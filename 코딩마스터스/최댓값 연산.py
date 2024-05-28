x, y, z = map(int, input().split())

def is_possible(x, y, z):
    max_value = max(x, y, z)
    
    if (x == max_value and y == max_value) or (y == max_value and z == max_value) or (x == max_value and z == max_value):
        return "possible"
    else:
        return "impossible"

print(is_possible(x, y, z))
