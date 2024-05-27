n = input()

hex_n = n[1:]
r = int(hex_n[0:2], 16)
g = int(hex_n[2:4], 16)
b = int(hex_n[4:6], 16)

avg = round((r+g+b) / 3)
gray = hex(avg)[2:].upper() 

if len(gray) == 1:
    gray = '0' + gray

print(f'#{gray*3}')
