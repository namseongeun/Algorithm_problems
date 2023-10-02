import sys

sys.stdin = open('1209_Sum.txt')

for _ in range(10):
    tc = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    diagonal_sum1 = 0
    diagonal_sum2 = 0

    for i in range(100):
        diagonal_sum1 += mat[i][i]
        diagonal_sum2 += mat[i][-i]

        if sum(mat[i]) > max_sum:
            max_sum = sum(mat[i])

    # 전치
    for i in range(100):
        for j in range(100):
            if i < j:
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(100):
        if sum(mat[i]) > max_sum:
            max_sum = sum(mat[i])
 
    print(f'#{tc} {max(max_sum, diagonal_sum1, diagonal_sum2)}')