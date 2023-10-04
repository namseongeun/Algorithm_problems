import sys


sys.stdin = open('4831_ElectricBus.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stations = list(map(int, input().split()))

    # 총 충전 횟수, 현재위치, 뒤로 돌아간 횟수 초기값
    cnt = 0
    tmp = K
    back_cnt = 0

    # 종점 도착전까지 반복
    while tmp < N:
        # 만약 현재 위치가 충전소라면 충전 한 번 하고 K만큼 앞으로 이동 후 뒤로 돌아간 횟수 리셋
        if tmp in charge_stations:
            cnt += 1
            tmp += K
            back_cnt = 0

        # 현재 위치가 충전소가 아니라면 바로 직전 위치 다음까지 하나씩 되짚어보기
        else:
            if back_cnt == (K-1):       # 만약 뒤로 돌아간 횟수가 K-1이라면 더 이상 앞으로 나아갈 수 없다고 판단
                break
            else:                   
                tmp -= 1
                back_cnt += 1


    if back_cnt == (K-1):
        answer = 0
    else: 
        answer = cnt

    print(f"#{tc} {answer}")