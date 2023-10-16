import sys


sys.stdin = open('1974_CheckSdoku.txt')

T = int(input())
for tc in range(1, T+1):
    Sdoku = [list(map(int, input().split())) for _ in range(9)]

    # 플래그 초기값 설정
    flag = 1

    # 열 중복 제거 후 검증
    for row in range(9):
        if len(set(Sdoku[row])) != 9:
            flag = 0

    # 전치
    for i in range(9):
        for j in range(9):
            if i < j:
                Sdoku[i][j], Sdoku[j][i] = Sdoku[j][i], Sdoku[i][j]

    # 행 중복 제거 후 검증
    for col in range(9):
        if len(set(Sdoku[col])) != 9:
            flag = 0

    # 3*3 격자 중복제거하여 검증
    for n in range(0, 7, 3):
        for m in range(0, 7, 3):
            if len(set(Sdoku[n][m:m+3] + Sdoku[n+1][m:m+3] + Sdoku[n+2][m:m+3])) != 9:
                flag = 0

    print(f'#{tc} {flag}')