import sys
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    graph[x][y] = 1
    count = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0:
            count += dfs(nx, ny)
    
    return count

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2): # 왼쪽 위 꼭짓점부터
        for j in range(y1, y2): # 오른쪽 아래 꼭짓점까지
            graph[i][j] = 1

result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result.append(dfs(i, j))
            
result.sort()
print(len(result))
for i in result:
    print(i, end=' ')