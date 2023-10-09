import sys


sys.stdin = open('4836_Coloring.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [[0]*10 for _ in range(10)]

    for _ in range(N):
        s_i, s_j, e_i, e_j, color = map(int, input().split())
        for n in range(s_i, e_i+1):
            for m in range(s_j, e_j+1):
                mat[n][m] += color

    cnt = 0
    for i in range(10):
        for j in range(10):
            if mat[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')