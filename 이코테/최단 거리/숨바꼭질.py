import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
# 시작 노드는 1
start = 1
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
q = []

for _ in range(m):
    a, b = map(int, input().split())
    # 이동 비용은 1
    graph[a].append((b, 1))
    graph[b].append((a, 1))
    
def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]  # 현재 노드까지의 거리인 dist와 연결된 노드까지의 거리 비용을 더한 것이
            if cost < distance[i[0]]:   # 연결된 노드의 최단 거리 테이블 값보다 작다면
                distance[i[0]] = cost   # 최단 거리 업데이트
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 최단 거리가 가장 먼 노드 번호
max_node = 0
# 도달할 수 있는 노드 중에서, 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
# 최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트
result = []

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
        
print(max_node, max_distance, len(result))