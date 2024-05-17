n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]  

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if graph[i]:
        print(' '.join(map(str, sorted(graph[i]))))
    else:
        print("no")
