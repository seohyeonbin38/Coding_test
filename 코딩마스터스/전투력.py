n = int(input())
k = list(map(int, input().split()))

k.sort(reverse=True)

max_sum = 0
for i in range(n):
    current_sum = k[i] * (i + 1)
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)
