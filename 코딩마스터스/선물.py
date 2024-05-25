import math
from functools import reduce

n = int(input())
a = list(map(int, input().split()))

def gcd_multiple(numbers):
    return reduce(math.gcd, numbers)

count = gcd_multiple(a)

print(count)
