def count_digits(start_day, holidays):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_index = {'SUN': 0, 'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6}
    start_day_index = day_index[start_day]
    
    # 색상별 숫자 사용 횟수
    red_count = [0] * 10
    blue_count = [0] * 10
    black_count = [0] * 10
    
    # 공휴일 저장
    holidays_set = set((month, day) for month, day in holidays)

    # 달력 생성 및 색상 할당
    current_day_index = start_day_index
    for month in range(1, 13):
        for day in range(1, days_in_month[month-1] + 1):
            if (month, day) in holidays_set or current_day_index == 0:  # 공휴일이거나 일요일인 경우 빨간색
                color = 'red'
            elif current_day_index == 6:  # 토요일인 경우 파란색
                color = 'blue'
            else:  # 그 외는 검은색
                color = 'black'
            
            # 날짜의 각 숫자에 대해 카운트 증가
            for digit in str(day):
                if color == 'red':
                    red_count[int(digit)] += 1
                elif color == 'blue':
                    blue_count[int(digit)] += 1
                else:
                    black_count[int(digit)] += 1
            
            # 다음 날짜로 이동
            current_day_index = (current_day_index + 1) % 7

    # 결과 출력
    for i in range(10):
        print(red_count[i], blue_count[i], black_count[i])


start_day = input()
n = int(input())
holidays = []
for i in range(n):
    a, b = map(int, input().split())
    holidays.append((a, b))

count_digits(start_day, holidays)
