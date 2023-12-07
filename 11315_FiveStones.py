import sys
import copy


sys.stdin = open('11315_FiveStones.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(input()) for _ in range(N)]

    n_grid = copy.deepcopy(grid)

    flag = 0

    for row in grid:
        for j in range(N-5+1):
            if row[j:j+5] == ['o'] * 5:
                flag += 1
                break

    for i in range(N):
        for j in range(N):
            if i < j:
                n_grid[i][j], n_grid[j][i] = n_grid[j][i], n_grid[i][j]

    for col in n_grid:
        for j in range(N-5+1):
            if col[j:j+5] == ['o'] * 5:
                flag += 1
                break

    
    i = 0
    while i != (N-5+1):
        for j in range(0, N-5+1):
            dia_1 = []
            for k in range(5):
                dia_1.append(grid[i+k][j+k])

            if dia_1 == ['o'] * 5:
                flag += 1
                break

        i += 1

    i = 0
    while i != (N-5+1):
        for j in range(0, N-5+1):
            dia_2 = []
            for k in range(5):
                dia_2.append(n_grid[i+k][j+k])
            
            if dia_2 == ['o'] * 5:
                flag += 1
                break

        i += 1

    if flag == 0:
        result = 'NO'
    else:  
        result = 'YES'

    print(f'#{tc} {result}')

    
