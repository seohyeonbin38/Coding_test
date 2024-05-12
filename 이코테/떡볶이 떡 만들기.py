n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 (왼쪽 탐색)
    if total < m:
        end = mid - 1
    else:
        result = mid    # 최대한 덜 잘랐을 때가 정답
        start = mid + 1
        
print(result)