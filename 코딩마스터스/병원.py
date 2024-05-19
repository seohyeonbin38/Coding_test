import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

def main():
    N = int(input())
    M = int(input())
    graph = {i: {} for i in range(1, N+1)}

    for _ in range(M):
        u, v, t = map(int, input().split())
        graph[u][v] = t
        graph[v][u] = t  

    S, E = map(int, input().split())

    distances = dijkstra(graph, S)
    print(distances[E])

if __name__ == "__main__":
    main()
