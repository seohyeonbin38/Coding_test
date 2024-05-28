grid = [input() for _ in range(4)]

def can_make_square(grid):
    # 마지막 컬럼은 고려x
    for i in range(3):
        for j in range(3):
            count_x = 0
            for k in range(2):
                for l in range(2):
                    if grid[i+k][j+l] == 'X':
                        count_x += 1
            if count_x >= 3:
                return "yes"
    return "no"

print(can_make_square(grid))
