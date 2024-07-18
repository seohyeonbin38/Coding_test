a, b, c = map(int, input().split())
time = [0] * 101
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        time[i] += 1
        
price = 0

for i in time:
    if i == 1:
        price += a
    elif i == 2:
        price += b*2
    elif i == 3:
        price += c*3

print(price)       