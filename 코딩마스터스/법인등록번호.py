def check_corporation_type(reg_front, reg_back, check_digit):
    # 오류검색번호 계산 함수
    def calculate_check_digit(numbers):
        A = sum(int(numbers[i]) for i in range(0, 12, 2))  # 홀수 번째 수의 합
        B = sum(int(numbers[i]) for i in range(1, 12, 2))  # 짝수 번째 수의 합
        R = (2 * B + A) % 10  # 나머지
        return (10 - R) % 10  # 오류검색번호

    # 법인 종류별 분류번호 범위
    types = {
        '상업 법인': range(11, 16),
        '민법 법인': range(21, 23),
        '특수 법인': range(31, 52),
        '외국 법인': range(81, 87),
        '기타 법인': [71]
    }

    result = ''

    for key, value in types.items():
        # 각 법인종류별로 검사
        match = False
        for type_code in value:
            # 법인종류별 분류번호를 가정하고 전체 번호를 재구성
            assumed_full_number = reg_front + str(type_code).zfill(2) + reg_back
            # 오류검색번호 계산
            calculated_check_digit = calculate_check_digit(assumed_full_number)
            if calculated_check_digit == check_digit:
                match = True
                break
        # 결과 문자열에 추가
        result += 'O' if match else 'X'

    return result

# 입력
reg_front = input().strip()  # 등기관서별 분류번호
reg_back = input().strip()   # 일련번호
check_digit = int(input().strip())  # 오류검색번호

# 법인 종류 판별
print(check_corporation_type(reg_front, reg_back, check_digit))
