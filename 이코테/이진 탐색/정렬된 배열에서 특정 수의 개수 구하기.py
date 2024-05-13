def count_by_value(array, m):
    n = len(array)
    
    # x가 처음 등장한 인덱스 계산
    a = first(array, m, 0, n - 1)
    
    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0
    
    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, m, 0, n - 1)
    
    return b - a + 1

# 처음 위치를 찾는 이진탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid + 1, end)
    
# 마지막 위치를 찾는 이진탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    else:
        return last(array, target, mid + 1, end)

n, m = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, m)

if count == 0:
    print(-1)
else:
    print(count)      
