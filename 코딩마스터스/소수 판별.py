import math
n = int(input())

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True 
    
if n != 1 and is_prime_number(n):
    print(1)
else:
    print(0)