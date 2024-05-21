# 히스토그램에서 최대 직사각형 찾기 알고리즘
def max_blessing(N, M, grid):
    max_bless = 0

    # 각 문자를 위한 히스토그램을 만든다.
    histograms = {chr(c): [0] * M for c in range(ord('A'), ord('Z') + 1)}

    for i in range(N):
        for j in range(M):
            for c in range(ord('A'), ord('Z') + 1):
                if grid[i][j] == chr(c):
                    histograms[chr(c)][j] += 1
                else:
                    histograms[chr(c)][j] = 0

        for c in range(ord('A'), ord('Z') + 1):
            max_bless = max(max_bless, max_histogram_area(histograms[chr(c)]))

    return max_bless

def max_histogram_area(histogram):
    stack = []
    max_area = 0
    index = 0
    
    while index < len(histogram):
        if not stack or histogram[stack[-1]] <= histogram[index]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (histogram[top_of_stack] * 
                   ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
    
    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] * 
               ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)
    
    return max_area

# 입력 받기
N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

# 결과 출력
print(max_blessing(N, M, grid))
