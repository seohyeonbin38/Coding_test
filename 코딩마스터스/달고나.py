def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or pan[x][y] == '1':  
        return False
    if pan[x][y] == '0':  
        pan[x][y] = '1'  
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())  
pan = [list(input()) for _ in range(n)]  

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)
