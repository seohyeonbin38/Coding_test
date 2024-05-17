n, k = map(int, input().split())
weight_value = []

for _ in range(n):
    m, v = map(int, input().split())
    weight_value.append((m,v))
    
weight_value.sort(key=lambda x: -x[1])

bag_limit = []    
for _ in range(k):
    c = int(input())
    bag_limit.append(c)

bag_limit.sort()

# 선택된 물건인지 확인
used = [False] * n
total = 0
for limit in bag_limit:
    for j in range(n):
        if not used[j] and limit >= weight_value[j][0]:
            total += weight_value[j][1]
            used[j] = True
            break
     
print(total)
    