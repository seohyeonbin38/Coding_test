n = int(input())
list = []
for i in range (n):
    y, x = map(int, input().split())
    list.append((y,x))

for i in range(len(list)):
    if i == (n - 1):
        break
    here_y = list[i][0]
    here_x = list[i][1]
    
    if (here_y < list[i+1][0]):
        print(1, list[i+1][0]-here_y)
    elif (here_y > list[i+1][0]):
        print(3, here_y-list[i+1][0])
    elif (here_x < list[i+1][1]):
        print(2, list[i+1][1]-here_x)
    elif (here_x > list[i+1][1]):
        print(4, here_x-list[i+1][1])