array = []
    
for _ in range(9):
    height = int(input())
    array.append(height)

array.sort()   

total = sum(array)
fakes = []

# 9명의 합에서 2명을 뺀 값이 100 이하인 경우 찾기
for i in range(9):
    for j in range(i+1, 9):
        if total - array[i] - array[j] == 100:
            fakes.append(array[i])
            fakes.append(array[j])
            break
            
for i in array:
    if i in fakes:
        continue
    print(i)
    