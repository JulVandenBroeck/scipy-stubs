from typing import Final, Literal

import numpy as np

_cospi: Final[np.ufunc] = ...
_iv_ratio: Final[np.ufunc] = ...
_iv_ratio_c: Final[np.ufunc] = ...
_lambertw: Final[np.ufunc] = ...
_log1mexp: Final[np.ufunc] = ...
_log1pmx: Final[np.ufunc] = ...
_riemann_zeta: Final[np.ufunc] = ...
_scaled_exp1: Final[np.ufunc] = ...
_sinpi: Final[np.ufunc] = ...
_spherical_in: Final[np.ufunc] = ...
_spherical_in_d: Final[np.ufunc] = ...
_spherical_jn: Final[np.ufunc] = ...
_spherical_jn_d: Final[np.ufunc] = ...
_spherical_kn: Final[np.ufunc] = ...
_spherical_kn_d: Final[np.ufunc] = ...
_spherical_yn: Final[np.ufunc] = ...
_spherical_yn_d: Final[np.ufunc] = ...
_zeta: Final[np.ufunc] = ...
airy: Final[np.ufunc] = ...
airye: Final[np.ufunc] = ...
assoc_legendre_p: Final[dict[tuple[bool, Literal[0, 1, 2]], np.ufunc]] = ...
bei: Final[np.ufunc] = ...
beip: Final[np.ufunc] = ...
ber: Final[np.ufunc] = ...
berp: Final[np.ufunc] = ...
besselpoly: Final[np.ufunc] = ...
beta: Final[np.ufunc] = ...
betaln: Final[np.ufunc] = ...
binom: Final[np.ufunc] = ...
cbrt: Final[np.ufunc] = ...
cosdg: Final[np.ufunc] = ...
cosm1: Final[np.ufunc] = ...
cotdg: Final[np.ufunc] = ...
dawsn: Final[np.ufunc] = ...
ellipe: Final[np.ufunc] = ...
ellipeinc: Final[np.ufunc] = ...
ellipj: Final[np.ufunc] = ...
ellipk: Final[np.ufunc] = ...
ellipkinc: Final[np.ufunc] = ...
ellipkm1: Final[np.ufunc] = ...
erf: Final[np.ufunc] = ...
erfc: Final[np.ufunc] = ...
erfcx: Final[np.ufunc] = ...
erfi: Final[np.ufunc] = ...
exp1: Final[np.ufunc] = ...
exp10: Final[np.ufunc] = ...
exp2: Final[np.ufunc] = ...
expi: Final[np.ufunc] = ...
expit: Final[np.ufunc] = ...
expm1: Final[np.ufunc] = ...
exprel: Final[np.ufunc] = ...
fresnel: Final[np.ufunc] = ...
gamma: Final[np.ufunc] = ...
gammainc: Final[np.ufunc] = ...
gammaincc: Final[np.ufunc] = ...
gammainccinv: Final[np.ufunc] = ...
gammaincinv: Final[np.ufunc] = ...
gammaln: Final[np.ufunc] = ...
gammasgn: Final[np.ufunc] = ...
hankel1: Final[np.ufunc] = ...
hankel1e: Final[np.ufunc] = ...
hankel2: Final[np.ufunc] = ...
hankel2e: Final[np.ufunc] = ...
hyp2f1: Final[np.ufunc] = ...
i0: Final[np.ufunc] = ...
i0e: Final[np.ufunc] = ...
i1: Final[np.ufunc] = ...
i1e: Final[np.ufunc] = ...
it2i0k0: Final[np.ufunc] = ...
it2j0y0: Final[np.ufunc] = ...
it2struve0: Final[np.ufunc] = ...
itairy: Final[np.ufunc] = ...
iti0k0: Final[np.ufunc] = ...
itj0y0: Final[np.ufunc] = ...
itmodstruve0: Final[np.ufunc] = ...
itstruve0: Final[np.ufunc] = ...
iv: Final[np.ufunc] = ...
ive: Final[np.ufunc] = ...
j0: Final[np.ufunc] = ...
j1: Final[np.ufunc] = ...
jv: Final[np.ufunc] = ...
jve: Final[np.ufunc] = ...
k0: Final[np.ufunc] = ...
k0e: Final[np.ufunc] = ...
k1: Final[np.ufunc] = ...
k1e: Final[np.ufunc] = ...
kei: Final[np.ufunc] = ...
keip: Final[np.ufunc] = ...
kelvin: Final[np.ufunc] = ...
ker: Final[np.ufunc] = ...
kerp: Final[np.ufunc] = ...
kv: Final[np.ufunc] = ...
kve: Final[np.ufunc] = ...
legendre_p: Final[tuple[np.ufunc, np.ufunc, np.ufunc]] = ...
log1p: Final[np.ufunc] = ...
log_expit: Final[np.ufunc] = ...
log_ndtr: Final[np.ufunc] = ...
log_wright_bessel: Final[np.ufunc] = ...
loggamma: Final[np.ufunc] = ...
logit: Final[np.ufunc] = ...
mathieu_a: Final[np.ufunc] = ...
mathieu_b: Final[np.ufunc] = ...
mathieu_cem: Final[np.ufunc] = ...
mathieu_modcem1: Final[np.ufunc] = ...
mathieu_modcem2: Final[np.ufunc] = ...
mathieu_modsem1: Final[np.ufunc] = ...
mathieu_modsem2: Final[np.ufunc] = ...
mathieu_sem: Final[np.ufunc] = ...
modfresnelm: Final[np.ufunc] = ...
modfresnelp: Final[np.ufunc] = ...
modstruve: Final[np.ufunc] = ...
ndtr: Final[np.ufunc] = ...
obl_ang1: Final[np.ufunc] = ...
obl_ang1_cv: Final[np.ufunc] = ...
obl_cv: Final[np.ufunc] = ...
obl_rad1: Final[np.ufunc] = ...
obl_rad1_cv: Final[np.ufunc] = ...
obl_rad2: Final[np.ufunc] = ...
obl_rad2_cv: Final[np.ufunc] = ...
pbdv: Final[np.ufunc] = ...
pbvv: Final[np.ufunc] = ...
pbwa: Final[np.ufunc] = ...
pro_ang1: Final[np.ufunc] = ...
pro_ang1_cv: Final[np.ufunc] = ...
pro_cv: Final[np.ufunc] = ...
pro_rad1: Final[np.ufunc] = ...
pro_rad1_cv: Final[np.ufunc] = ...
pro_rad2: Final[np.ufunc] = ...
pro_rad2_cv: Final[np.ufunc] = ...
psi: Final[np.ufunc] = ...
radian: Final[np.ufunc] = ...
rgamma: Final[np.ufunc] = ...
sindg: Final[np.ufunc] = ...
sph_harm: Final[np.ufunc] = ...
sph_harm_y: Final[tuple[np.ufunc, np.ufunc, np.ufunc]] = ...
sph_legendre_p: Final[tuple[np.ufunc, np.ufunc, np.ufunc]] = ...
struve: Final[np.ufunc] = ...
tandg: Final[np.ufunc] = ...
voigt_profile: Final[np.ufunc] = ...
wofz: Final[np.ufunc] = ...
wright_bessel: Final[np.ufunc] = ...
xlog1py: Final[np.ufunc] = ...
xlogy: Final[np.ufunc] = ...
y0: Final[np.ufunc] = ...
y1: Final[np.ufunc] = ...
yv: Final[np.ufunc] = ...
yve: Final[np.ufunc] = ...
zetac: Final[np.ufunc] = ...

def _set_action(code: int, action: int, /) -> None: ...
