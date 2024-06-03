import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(m+1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
    
def dijkstra(start):
    q = []
    # 첫 번째 원소를 기준으로 정렬되므로 비용이 첫 번째
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # heapq에서 꺼낸 가장 짧은 노드의 길이가 기존 distance에 저장된 길이보다 길 경우, 계산할 필요가 없음
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)

# 도달할 수 있는 노드 수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1
print(count - 1, max_distance)