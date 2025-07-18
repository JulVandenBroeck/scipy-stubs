from _typeshed import IdentityFunction
from collections.abc import Callable
from typing import Literal as L, TypeAlias, overload

import numpy as np
import optype.numpy as onp

_Inexact: TypeAlias = np.float64 | np.complex128

_FloatND: TypeAlias = onp.ArrayND[np.float64]
_InexactND: TypeAlias = onp.ArrayND[np.float64 | np.complex128]

###
# Undocumented (private) functions
# (we can't ignore thes, as there's no `__all__` (at runtime) in this module)

#
def use_reflection(
    sign_n_even: L[1, -1] | None = None,
    reflection_fun: Callable[[int, complex, bool], onp.ToComplex] | None = None,  # should accept the four public functions below
) -> IdentityFunction: ...  # undocumented

# defined as `(n, z, derivative=False) -> spherical_kn(n, z, derivative=).real`
@overload  # (int, complex) -> float
def spherical_kn_reflection(n: onp.ToInt, z: onp.ToComplex, derivative: bool = False) -> np.float64: ...
@overload  # (int, complex[:, ...]) -> float[:, ...]
def spherical_kn_reflection(n: onp.ToInt, z: onp.ToComplexND, derivative: bool = False) -> _FloatND: ...
@overload  # (int[:, ...], complex[...]) -> float[:, ...]
def spherical_kn_reflection(n: onp.ToIntND, z: onp.ToComplex | onp.ToComplexND, derivative: bool = False) -> _FloatND: ...

###
# Public functions.
# (with identical signatures)

#
@overload  # (int, float) -> float
def spherical_jn(n: onp.ToInt, z: onp.ToFloat, derivative: bool = False) -> np.float64: ...
@overload  # (int, float[:, ...]) -> float[:, ...]
def spherical_jn(n: onp.ToInt, z: onp.ToFloatND, derivative: bool = False) -> _FloatND: ...
@overload  # (int[:, ...], float[...]) -> float[:, ...]
def spherical_jn(n: onp.ToIntND, z: onp.ToFloat | onp.ToFloatND, derivative: bool = False) -> _FloatND: ...
@overload  # (int, complex) -> complex
def spherical_jn(n: onp.ToInt, z: onp.ToComplex, derivative: bool = False) -> _Inexact: ...
@overload  # (int, complex[:, ...]) -> complex[:, ...]
def spherical_jn(n: onp.ToInt, z: onp.ToComplexND, derivative: bool = False) -> _InexactND: ...
@overload  # (int[:, ...], complex[...]) -> complex[:, ...]
def spherical_jn(n: onp.ToIntND, z: onp.ToComplex | onp.ToComplexND, derivative: bool = False) -> _InexactND: ...

#
@overload  # (int, float) -> float
def spherical_yn(n: onp.ToInt, z: onp.ToFloat, derivative: bool = False) -> np.float64: ...
@overload  # (int, float[:, ...]) -> float[:, ...]
def spherical_yn(n: onp.ToInt, z: onp.ToFloatND, derivative: bool = False) -> _FloatND: ...
@overload  # (int[:, ...], float[...]) -> float[:, ...]
def spherical_yn(n: onp.ToIntND, z: onp.ToFloat | onp.ToFloatND, derivative: bool = False) -> _FloatND: ...
@overload  # (int, complex) -> complex
def spherical_yn(n: onp.ToInt, z: onp.ToComplex, derivative: bool = False) -> _Inexact: ...
@overload  # (int, complex[:, ...]) -> complex[:, ...]
def spherical_yn(n: onp.ToInt, z: onp.ToComplexND, derivative: bool = False) -> _InexactND: ...
@overload  # (int[:, ...], complex[...]) -> complex[:, ...]
def spherical_yn(n: onp.ToIntND, z: onp.ToComplex | onp.ToComplexND, derivative: bool = False) -> _InexactND: ...

#
@overload  # (int, float) -> float
def spherical_in(n: onp.ToInt, z: onp.ToFloat, derivative: bool = False) -> np.float64: ...
@overload  # (int, float[:, ...]) -> float[:, ...]
def spherical_in(n: onp.ToInt, z: onp.ToFloatND, derivative: bool = False) -> _FloatND: ...
@overload  # (int[:, ...], float[...]) -> float[:, ...]
def spherical_in(n: onp.ToIntND, z: onp.ToFloat | onp.ToFloatND, derivative: bool = False) -> _FloatND: ...
@overload  # (int, complex) -> complex
def spherical_in(n: onp.ToInt, z: onp.ToComplex, derivative: bool = False) -> _Inexact: ...
@overload  # (int, complex[:, ...]) -> complex[:, ...]
def spherical_in(n: onp.ToInt, z: onp.ToComplexND, derivative: bool = False) -> _InexactND: ...
@overload  # (int[:, ...], complex[...]) -> complex[:, ...]
def spherical_in(n: onp.ToIntND, z: onp.ToComplex | onp.ToComplexND, derivative: bool = False) -> _InexactND: ...

#
@overload  # (int, float) -> float
def spherical_kn(n: onp.ToInt, z: onp.ToFloat, derivative: bool = False) -> np.float64: ...
@overload  # (int, float[:, ...]) -> float[:, ...]
def spherical_kn(n: onp.ToInt, z: onp.ToFloatND, derivative: bool = False) -> _FloatND: ...
@overload  # (int[:, ...], float[...]) -> float[:, ...]
def spherical_kn(n: onp.ToIntND, z: onp.ToFloat | onp.ToFloatND, derivative: bool = False) -> _FloatND: ...
@overload  # (int, complex) -> complex
def spherical_kn(n: onp.ToInt, z: onp.ToComplex, derivative: bool = False) -> _Inexact: ...
@overload  # (int, complex[:, ...]) -> complex[:, ...]
def spherical_kn(n: onp.ToInt, z: onp.ToComplexND, derivative: bool = False) -> _InexactND: ...
@overload  # (int[:, ...], complex[...]) -> complex[:, ...]
def spherical_kn(n: onp.ToIntND, z: onp.ToComplex | onp.ToComplexND, derivative: bool = False) -> _InexactND: ...
