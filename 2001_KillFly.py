import sys


sys.stdin = open('2001_KillFly.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly_mat = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill_cnt = 0

            for m in range(M):
                kill_cnt += sum(fly_mat[i + m][j: j+M])

            if kill_cnt > max_kill:
                max_kill = kill_cnt

    print(f'#{tc} {max_kill}')