n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1):
    graph[i].sort()
    
visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
dfs(1)