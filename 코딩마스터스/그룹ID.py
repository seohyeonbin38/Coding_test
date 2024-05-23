def dfs(vertex, visited, graph):
    visited.add(vertex)
    group.append(vertex)
    if vertex in graph:  
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor, visited, graph)

N, M = map(int, input().split())
graph = {}

for _ in range(M):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

visited = set()
max_group_size = 0
min_group_id = N + 1

for i in range(1, N + 1):
    if i not in visited:
        group = []
        dfs(i, visited, graph)
        if len(group) > max_group_size:
            max_group_size = len(group)
            min_group_id = min(group)
        elif len(group) == max_group_size:
            min_group_id = min(min_group_id, min(group))

print(min_group_id)
