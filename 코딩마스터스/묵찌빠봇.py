from math import gcd

# 최소 공배수(LCM)를 구하는 함수
def lcm(x, y):
    return x * y // gcd(x, y)

# 묵찌빠 게임의 손 모양 정의
def determine_winner(move1, move2):
    if move1 == move2:
        return 0  # 비김
    elif (move1 == 1 and move2 == 3) or (move1 == 2 and move2 == 1) or (move1 == 3 and move2 == 2):
        return 1  # move1 승리
    else:
        return 2  # move2 승리

# 입력 받기
N, M = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# 가위바위보로 선공과 후공 결정
idx1, idx2 = 0, 0
first_winner = 0
while idx1 < N and idx2 < M:
    move1 = list1[idx1 % N]
    move2 = list2[idx2 % M]
    result = determine_winner(move1, move2)
    if result != 0:
        first_winner = result
        break
    idx1 += 1
    idx2 += 1

# 첫 승리자가 없는 경우
if first_winner == 0:
    print(0)
else:
    # 묵찌빠 게임 진행 (가위바위보에서 이미 승자가 결정됨)
    current_turn = first_winner
    max_cycles = lcm(N, M)

    # 최소 공배수까지 승부가 나지 않는 경우를 확인하기 위해 idx1, idx2를 업데이트
    idx1 += 1
    idx2 += 1

    for _ in range(1, max_cycles):
        move1 = list1[idx1 % N]
        move2 = list2[idx2 % M]
        result = determine_winner(move1, move2)
        
        # 비긴 경우, 현재 승리자 출력
        if result == 0:
            print(current_turn)
            break
        elif result != current_turn:  # 선공이 이기지 않은 경우, 턴 교체
            current_turn = 3 - current_turn

        idx1 += 1
        idx2 += 1
    else:
        # 최소 공배수까지 승부가 나지 않는 경우, 승부가 나지 않음
        print(0)
