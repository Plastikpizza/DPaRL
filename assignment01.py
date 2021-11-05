#! /usr/bin/python3
from functools import lru_cache
from math import e, pow
from sys import setrecursionlimit, maxsize

C = 100
T = 600

def Σ(i, to, fn):
    s = 0
    for ii in range(i, to+1):
        s += fn(ii)
    return s

f = lambda i : [  500,   300,    200][i-1]
μ = lambda i : [0.001, 0.015,   0.05][i-1]
υ = lambda i : [ 0.01, 0.005, 0.0025][i-1]
λ = lambda t, i : μ(i)*pow(e, υ(i)*t)

@lru_cache(maxsize=4096)
def V(t, x):
    if 1 <= t and t <= T and x != 0:
        return max([(f(a) + V(t+1, x-1)) * Σ(i=1, to=a, fn=lambda i: λ(t, i))
                + (1-Σ(i=1, to=a, fn=lambda i: λ(t, i))) * V(t+1, x)
                for a in range(1,4)])
    return 0

if __name__ == "__main__":
    setrecursionlimit(8192)
    # values = {}
    # for x in range(1, 101):
    #     for t in range(1, 601):
    #         values[(t, x)] = V(t,x)
    print(V(1, C))