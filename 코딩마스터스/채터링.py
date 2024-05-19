n, k = map(int, input().split())
alpha = input()
alpha = list(alpha)

for i in range(len(alpha)):
    print((alpha[i] * k), end='')