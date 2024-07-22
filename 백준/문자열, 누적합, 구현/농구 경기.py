n = int(input())
players = [0] * 26

for i in range(n):
    name = input()
    first_name = name[0]
    players[ord(first_name) - ord('a')] += 1

result = False   
for i in range(len(players)):
    if players[i] >= 5:
        print(chr(97+i), end='')
        result = True

if result == False:
    print('PREDAJA')
