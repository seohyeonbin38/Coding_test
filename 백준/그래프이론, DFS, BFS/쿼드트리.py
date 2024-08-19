n = int(input())

tree = [list(map(int, input())) for _ in range(n)]
result = []

def quadtree(x, y, n):
    color = tree[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != tree[i][j]: # 범위 안에서 한 개라도 다른 경우, 4분면으로 나눠서 다시 탐색
                result.append('(')  # 4분면으로 분할할때 괄호를 친다.
                quadtree(x, y, n//2)  
                quadtree(x, y+n//2, n//2)  
                quadtree(x+n//2, y, n//2)
                quadtree(x+n//2, y+n//2, n//2)
                result.append(')')
                return
    result.append(color)  # 재귀로 들어가지 않고 for문이 다 끝났기 때문에 범위 안에 모든 수가 같다.

quadtree(0, 0, n)
print(''.join(map(str, result)))