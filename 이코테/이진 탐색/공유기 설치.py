n, c = map(int(), input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = 1   # 가능한 최소 거리
end = array[-1] - array[0]  # 가능한 최대 거리

while(start <= end):
    mid = (start + end) // 2    # mid는 가장 인접한 두 공유기 사이의 거리
    value = array[0]
    count = 1
    for i in range(1, n):   # 앞에서부터 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
            
    if count >= c:  # c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid    # 최적의 결과 저장
    else:   # c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1

print(result)
