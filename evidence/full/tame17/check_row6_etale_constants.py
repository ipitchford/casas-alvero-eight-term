"""Exact arithmetic for the bounded row-6 unramified-lifting audit."""
from math import comb
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def hv(h, k, x):
    return sum(c*comb(e, k)*pow(x, e-k, 17)
               for e, c in h.items() if e >= k) % 17


h = {20: 1, 18: 14, 17: 2, 2: 11, 1: 6}
require([hv(h,k,6) for k in (0,1,2)] == [0,3,0], "Wrong simple H2 witness")
require([hv(h,k,10) for k in (0,1,2)] == [0,0,5], "Wrong double cluster")
require(hv(h,1,0) == 6 and hv(h,1,1) == 11, "Special roots not simple")
a18_s = (-18*pow(6,17,17)) % 17
a19_s = -190*pow(20,-1,17)*a18_s % 17
require([a18_s,a19_s] == [11,6], "Eliminated coefficient slopes")
total_s = (hv(h,1,6)+190*a18_s*6**2+20*a19_s*6) % 17
critical_r = 2*hv(h,2,10)*pow(20,-1,17) % 17
critical_s = (380*a18_s*10+20*a19_s)*pow(20,-1,17) % 17
require([total_s,critical_r,critical_s] == [7,9,5], "Root-block entries")
for j in range(4,17):
    require(comb(18,j) % 17 == comb(20,j) % 17 == 0,
            "A coefficient-parameter derivative survives reduction")
require((1-190+2280) == 2091, "f(1) fixed part")
require((-pow(6,18,17)) % 17 == 15, "a18 residue")
require((-2091-190*15)*pow(20,-1,17) % 17 == 2, "a19 residue")
print(json.dumps({"status":"PASS", "sResidue":6,"rResidue":10,
                  "a18_sMod17":a18_s,"a19_sMod17":a19_s,
                  "totalDerivative_fOfs":total_s,
                  "criticalDerivative_r":critical_r,
                  "criticalDerivative_s":critical_s,
                  "scope":"Exact local arithmetic; structural proof in ROW6_ETALE_AUDIT.md"},indent=2))
