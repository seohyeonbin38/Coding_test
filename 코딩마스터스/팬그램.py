n = input()
n = n.lower()

alphabet = set()

for char in n:
    alphabet.add(char)

if len(alphabet) == 26:
    print("YES")
else:
    print("NO")
