import sys


sys.stdin = open('0214_Snail.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [[0] * N for _ in range(N)]

    num = 1
    start = 0
    end = N-1
    i = j = 0

    while num <= N**2:
        # 윗면인 경우 우상단 도착시 방향을 틀고 아니면 오른쪽으로 진행
        if i == start:
            if j == end:
                mat[i][j] = num
                num += 1
                i += 1
            else:
                mat[i][j] = num
                num += 1
                j += 1

        # 오른면인 경우 우하단 도착시 방향을 틀고 아니면 아래쪽으로 진행
        elif j == end:
            if i == end:
                mat[i][j] = num
                num += 1
                j -= 1
            else:
                mat[i][j] = num
                num += 1
                i += 1            

        # 아랫면인 경우 좌하단 도착시 방향을 틀고 아니면 왼쪽으로 진행
        elif i == end:
            if j == start:
                mat[i][j] = num
                num += 1
                i -= 1
            else:
                mat[i][j] = num
                num += 1
                j -= 1

        # 왼면인 경우 좌상단 도착시 방향을 틀고 아니면 위로 진행
        elif j == start:
            if i == (start + 1):
                mat[i][j] = num
                num += 1
                start += 1
                end -= 1
                j += 1
            else:
                mat[i][j] = num
                num += 1
                i -= 1

    print(f"#{tc}")
    for ls in mat:
        print(*ls)