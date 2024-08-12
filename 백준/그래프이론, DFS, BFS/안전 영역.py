import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = []
max_num = 0
result = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, num):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n) and visited[nx][ny] == 0:
            if graph[nx][ny] > num:
                visited[nx][ny] = 1
                dfs(nx, ny, num)               

for i in range(n):
    place = list(map(int, input().split()))
    graph.append(place)

    # 최고 높이가 얼마인지 확인
    for j in place:
        if j > max_num:
            max_num = j

# 최고 높이까지 오면 모두 잠기기 때문에 최고 높이-1 까지만 계산
for i in range(max_num):
    visited = [[0] * n for _ in range(n)]
    count = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                count += 1
                visited[j][k] = 1
                dfs(j,k,i)
    result = max(result, count)

print(result)