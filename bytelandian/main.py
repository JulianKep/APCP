from functools import *


@cache
def split(n):

    half = n//2
    third = n//3
    quarter = n//4

    sum = half + third + quarter

    if (sum >= n):
        return n

    return max(split(half), half) + max(split(third), third) + max(split(quarter), quarter)



print(split(12))