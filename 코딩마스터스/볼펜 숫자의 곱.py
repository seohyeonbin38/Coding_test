n = int(input())
pens = list(map(int, input().split()))

pos = sorted([x for x in pens if x > 0], reverse=True)
neg = sorted([x for x in pens if x < 0])
zero = [x for x in pens if x == 0]

results = []

if len(pos) >= 3:
    results.append(pos[0] * pos[1] * pos[2])
elif len(pos) > 0 and len(neg) >= 2:
    results.append(pos[0] * neg[0] * neg[1])
elif len(pos) >= 2:
    results.append(pos[0] * pos[1])
elif len(pos) == 0 and len(neg) >= 2:
    results.append(neg[0] * neg[1])

if results:
    print(max(results))
else:
    print(0)