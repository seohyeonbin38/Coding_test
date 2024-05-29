n = list(input())
m = list(input())

og = {}
new = {}

for num in n:
    if num in og:
        og[num] += 1
    else:
        og[num] = 1

for num in m:
    if num in new:
        new[num] += 1
    else:
        new[num] = 1

if og == new:
    print('YES')
else:
    print('NO')