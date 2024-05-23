import math

a, b, c = map(int, input().split())

x = 10 * c / a
x = math.ceil(x)

print(x)
