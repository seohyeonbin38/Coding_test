s = input()

count1 = 0
count_num = 0
for i in range(len(s)):
    if s[i] == '-':
        count1 += 1
    else:
        count_num += 1
        
if (s[0] == '0') and (s[1] == '1') and (s[2] == '0') and (count1 == 2) and (count_num == 11):
    print('valid')
else:
    print('invalid')