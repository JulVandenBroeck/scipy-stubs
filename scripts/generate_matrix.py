# ruff: noqa: TRY003

import importlib.metadata
import json
import subprocess  # noqa: S404
import sys
import urllib.error
import urllib.request
from functools import cache
from typing import Any, Final, TypedDict, cast

from packaging.specifiers import SpecifierSet
from packaging.version import Version, parse

INDENT: Final = 4
PACKAGE_NAME: Final = "scipy"
DEPENDENCY_NAME: Final = "numpy"
MIN_VERSIONS: Final = (
    (Version("3.11"), Version("1.25")),
    (Version("3.12"), Version("1.26")),
    (Version("3.13"), Version("2.1")),
)


class UVPythonVersionParts(TypedDict):
    major: int
    minor: int
    patch: int


class UVPythonRelease(TypedDict):
    name: str
    version: str
    version_parths: UVPythonVersionParts
    path: str | None
    symlink: str | None
    url: str | None
    os: str
    variant: str
    implementation: str
    arch: str
    libc: str


class FileInfo(TypedDict, total=False):
    filename: str
    arch: str
    platform: str
    platform_version: str | None
    download_url: str
    requires_python: str


class Release(TypedDict):
    version: str
    stable: bool
    release_url: str
    files: list[FileInfo]


class PackageVersions(TypedDict, total=False):
    releases: dict[str, list[FileInfo]]


@cache
def get_package_minimum_python_version(package: str) -> Version:
    """
    Get the minimum Python version required by the specified package.

    Args:
        package (str): The name of the package.

    Returns:
        Version: The minimum Python version required by the package as specified
                 in its metadata.

    Raises:
        KeyError: If 'Requires-Python' is not specified in the package metadata.
        NotImplementedError: If the version specifier contains an upper bound.

    """
    raw_version = importlib.metadata.metadata(package)["Requires-Python"]
    if "<" in raw_version:
        raise NotImplementedError(
            "Version specifier with upper bound not yet supported!"
        )

    return parse(raw_version.replace(">=", "").replace("~=", ""))


def get_dependency_minimum_version(package: str, dependency: str) -> Version:
    """
    Get the minimum version of a dependency required by the specified package.

    Args:
        package (str): The name of the package.
        dependency (str): The name of the dependency.

    Returns:
        Version: The minimum required version of the dependency.

    Raises:
        ValueError:
            The package does not list any requirements or the dependency is not found.

    """
    requirements = importlib.metadata.requires(package)
    if not requirements:
        raise ValueError(f"No requirements for {package}")

    try:
        # Find the first requirement that matches the dependency and is not an extra
        dependency_req = next(
            req
            for req in requirements
            if req.startswith(dependency) and " extra " not in req
        )
    except StopIteration as e:
        raise ValueError(
            f"Dependency {dependency} not found in requirements for {package}"
        ) from e

        # Extract the version specifier (e.g., ">=1.21.0")
    version_specifier = next(
        (ver for ver in dependency_req.split(",") if ">" in ver), None
    )
    if version_specifier is None:
        raise ValueError(
            f"No version specifier found for dependency {dependency} in {package}"
        )

    # Remove dependency name and comparison operator to get the version
    version_str = (
        version_specifier.replace(dependency, "").replace(">=", "").replace(">", "")
    )
    return parse(version_str)


def get_available_python_versions(
    min_version: Version | None = None,
    max_version: Version | None = None,
    pre_releases: bool = False,
) -> list[Version]:
    """
    Get a list of available Python versions from GitHub Actions' Python Versions
    Manifest.

    Args:
        min_version (Version | None): The minimum Python version to include in the list.
        max_version (Version | None): The maximum Python version to include in the list.
        pre_releases (bool): Whether to include pre-release versions.

    Returns:
        list[Version]:
            A list of available Python versions satisfying the specified criteria.

    Raises:
        urllib.error.URLError: If fetching data fails.

    """
    data_raw = subprocess.check_output(["uv", "python", "list", "--output-format=json"])  # noqa: S607
    data = cast("list[UVPythonRelease]", json.loads(data_raw))

    versions: dict[tuple[int, int], Version] = {}

    for release in data:
        if release["implementation"] != "cpython" or release["variant"] != "default":
            continue

        version = parse(release["version"])
        if version.is_prerelease and not pre_releases:
            continue

        if min_version and version < min_version:
            continue
        if max_version and version > max_version:
            continue

        version_tuple = version.major, version.minor
        if version_tuple < MIN_VERSIONS[0][0].release[:2]:
            continue

        versions[version_tuple] = version

    return sorted(versions.values())


@cache
def fetch_json(url: str) -> Any:
    """
    Fetch JSON data from a URL with caching.

    Args:
        url (str): The URL to fetch.

    Returns:
        dict[str, Any] | list[Any]: The parsed JSON data.

    Raises:
        urllib.error.URLError: If fetching data fails.

    """
    try:
        with urllib.request.urlopen(url) as response:  # noqa: S310
            return json.loads(response.read())
    except urllib.error.URLError as e:
        print(e, file=sys.stderr)  # noqa: T201
        sys.exit(1)


def get_available_package_versions(
    package_name: str, min_version: Version, pre_releases: bool = False
) -> dict[Version, str]:
    """
    Get available package versions from PyPI starting from the specified minimum
    version, but only include the latest micro version within each minor version series,
    along with their 'requires_python' specifiers.

    Args:
        package_name (str): The name of the package on PyPI.
        min_version (Version): The minimum version to include.

    Returns:
        dict[Version, str]:
            A mapping from the latest package versions in each minor version series to
            their 'requires_python' specifier.

    Raises:
        RuntimeError: If no 'requires_python' is found for a package version.

    """
    data: PackageVersions = fetch_json(f"https://pypi.org/pypi/{package_name}/json")

    releases = data.get("releases", {})
    latest_versions: dict[tuple[int, int], tuple[Version, str]] = {}
    for version_str, release_files in releases.items():
        version = parse(version_str)
        if version < min_version or (version.is_prerelease and not pre_releases):
            continue

            # Get 'requires_python' for this version
        requires_python = None
        for file_info in release_files:
            if "requires_python" in file_info:
                requires_python = file_info["requires_python"]
                if requires_python:
                    break

        if requires_python is None:
            # Skip versions without 'requires_python'
            continue

        key = version.major, version.minor
        # Update to latest version within the minor version series
        if key not in latest_versions or version > latest_versions[key][0]:
            latest_versions[key] = version, requires_python

        # Extract the versions and requires_python from the latest_versions dict
    return dict(latest_versions.values())


def main() -> None:
    """
    Main function to generate and output the test matrix.

    This function fetches the minimum required Python version for the package
    ('PACKAGE_NAME'), gets the list of available Python versions starting from
    that minimum version, and fetches the available versions of the dependency
    ('DEPENDENCY_NAME') starting from the minimum version required by the package.

    It then computes a matrix of combinations of Python versions and dependency
    versions that are compatible according to the 'requires_python' specifiers.

    Outputs:
        A JSON object representing the test matrix, printed to stdout.

    """
    min_py = get_package_minimum_python_version(PACKAGE_NAME)
    versions_py = get_available_python_versions(min_py)

    min_np = get_dependency_minimum_version(PACKAGE_NAME, DEPENDENCY_NAME)
    versions_np = get_available_package_versions(DEPENDENCY_NAME, min_np)

    matrix_entries: list[dict[str, str]] = []
    for np_version, py_requires in versions_np.items():
        py_spec = SpecifierSet(py_requires)

        for py_version in versions_py:
            if py_version not in py_spec:
                continue

            # Skip incompatible combinations
            if any(
                py_version >= py_min and np_version < np_min
                for py_min, np_min in MIN_VERSIONS
            ):
                continue

            matrix_entries.append({
                "python": f"{py_version.major}.{py_version.minor}",
                DEPENDENCY_NAME: f"{np_version.major}.{np_version.minor}",
            })  # fmt: skip

    json.dump({"include": matrix_entries}, indent=INDENT, fp=sys.stdout)
    _ = sys.stderr.flush()
    _ = sys.stdout.flush()


if __name__ == "__main__":
    main()
