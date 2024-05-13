a, b = map(int, input().split())
n, m = map(int, input().split())

options = []
for _ in range(n):
    options.append(int(input()))

options.sort(reverse=True)

total=0
for i in range(0, m):
    total += options[i]

print('total : ', total)
    
result = a + b * total
print(result)
    