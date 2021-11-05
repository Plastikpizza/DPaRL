#! /usr/bin/python3
from functools import lru_cache
from math import e, pow
from sys import setrecursionlimit, maxsize

# we define an interval to be the range of numbers from start to (and including)
# end. Notice: python's range does not include the upper bound.
interval = lambda start, end : range(start, end+1)

# the constants from the assignment document:
C = 100
T = 600

# a mathematical summation is defined like this.
# We use it to make our calculation look more like the one on the slides.
Σ = lambda i, to, fn : sum(map(fn, interval(i, to)))

# in the slides, all indices start at 1 while in python indices are 0-based.
# To be able to still use the notation/version on the slides, we use the
# "functions" below to effectively make our list indices appear to
# start at 1.
f = lambda i : [  500,   300,    200][i-1]
μ = lambda i : [0.001, 0.015,   0.05][i-1]
υ = lambda i : [ 0.01, 0.005, 0.0025][i-1]
λ = lambda t, i : μ(i)*pow(e, υ(i)*t)

# this next line tells python to cache/remember function values already 
# computed by the V-function. 
# Below that is just the function definition. We keep it VERY close to the
# one that we can find on the slides.
@lru_cache(maxsize=4096) 
def V(t, x):
    if 1 <= t and t <= T and x != 0:
        return max([(f(a) + V(t+1, x-1)) * Σ(i=1, to=a, fn=lambda i: λ(t, i))
                + (1-Σ(i=1, to=a, fn=lambda i: λ(t, i))) * V(t+1, x)
                for a in range(1,4)])
    return 0

# this line tells python to only execute the indented program when
# the file is executed directly and not when it is imported by e.g.
# another file.
if __name__ == "__main__":
    # functions can usually only call themselfs for a limited number of times
    # in python. The following line tells python to increase that number.
    setrecursionlimit(8192)

    # we build the V-table in the following part. 
    # values : (time, state) -> V-value
    vTable = {}
    for x in interval(1, 100):
        for t in interval(1, 600):
            vTable[(t, x)] = V(t,x)
    
    print("Task 1) ${:.2f}".format(vTable.get((1, C))))