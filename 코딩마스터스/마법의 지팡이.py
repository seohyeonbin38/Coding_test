from collections import deque

def bfs(n):
    if n == 1:
        return 0
    
    visited = set()
    queue = deque([(n, 0)])
    
    while queue:
        cur, count = queue.popleft()
        
        if cur == 1:
            return count
        
        if cur in visited:
            continue
        
        visited.add(cur)
        
        if cur % 2 == 0:
            queue.append((cur // 2, count + 1))
        if cur % 3 == 0:
            queue.append((cur // 3 * 2, count + 1))
        if cur % 5 == 0:
            queue.append((cur // 5 * 4, count + 1))
            
    return -1

n = int(input())
print(bfs(n))