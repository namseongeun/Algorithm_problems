import sys


sys.stdin = open('1959_TwoNums.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        max_multiple = float('-inf')
        for i in range(M - N + 1):
            sum_multiple = 0
            for j in range(N):
                sum_multiple += A[0+j] * B[i+j]
            if sum_multiple > max_multiple:
                max_multiple = sum_multiple

        print(f"#{tc} {max_multiple}")

    else:
        max_multiple = float('-inf')
        for i in range(N - M + 1):
            sum_multiple = 0
            for j in range(M):
                sum_multiple += B[0 + j] * A[i + j]
            if sum_multiple > max_multiple:
                max_multiple = sum_multiple

        print(f"#{tc} {max_multiple}")
