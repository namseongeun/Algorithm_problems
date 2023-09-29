import sys


sys.stdin = open('1210_Ladder.txt')

for _ in range(10):
    tc = int(input())
    ladder_mat = [list(map(int, input().split())) for _ in range(100)]

    i = 99
    j = 0
    for e in range(100):
        if ladder_mat[99][e] == 2:
            j = e

    while i >= 0:
        # 좌로 빠지는지
        if 0 <= (j-1) < 100 and ladder_mat[i][j-1] == 1:
            ladder_mat[i][j] = 0
            j -= 1

        # 우로 빠지는지
        elif 0 <= (j+1) < 100 and ladder_mat[i][j+1] == 1:
            ladder_mat[i][j] = 0
            j += 1

        # 위로 빠지는지
        else: 
            i -= 1

    print(f"#{tc} {j}")