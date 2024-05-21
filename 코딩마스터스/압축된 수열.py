def convert_to_base(num, base):
    if num == 0:
        return "0"
    digits = []
    while num:
        remain = num % base
        if remain < 10:
            digits.append(str(remain))
        elif remain < 36:
            digits.append(chr(remain - 10 + ord('A')))
        else:
            digits.append(chr(remain - 36 + ord('a')))
        num //= base
    return ''.join(digits[::-1])

def calculate_file_size(numbers, base):
    total_length = 0
    for num in numbers:
        total_length += len(convert_to_base(num, base))
    total_length += len(numbers) - 1  # 공백의 수
    return total_length

def find_minimum_base(N, M, numbers):
    for base in range(10, 63):
        if calculate_file_size(numbers, base) <= M:
            return base
    return -1

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

print(find_minimum_base(n, m, numbers))
