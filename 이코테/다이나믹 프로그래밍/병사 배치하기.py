n = int(input())
array = list(map(int, input().split()))

# 순서를 뒤집어서 가장 긴 증가하는 부분 수열 문제로 전환
array.reverse()

dp = [1] * n

for i in range(1,n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(n - max(dp))