n, m = map(int, input().split())
list = []

for _ in range(m):
    a, b = map(int, input().split())
    list.append([a,b])
    
k = int(input())
pos = k

for move in list:
    if move[0] == pos:
        pos = move[1]
    elif move[1] == pos:
        pos = move[0]


print(pos)