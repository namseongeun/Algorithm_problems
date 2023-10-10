import sys


sys.stdin = open('1979_WhereWord.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    word_grid = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0 
    
    # 조건 1. 행의 끝 K개가 전부 1이고 그 직전 값은 0
    # 조건 2. 행의 시작에서부터 K개가 전부 1이고 그 직후 값이 0
    # 조건 3. 그 사이에서 K개가 전부 1이면서 직전, 직후 값이 0

    # 행
    for row in word_grid:
        for i in range(N-K+1):
            if ( i == (N-K) ) and ( row[i-1] == 0 ) and ( row[i:] == [1]*K ):
                cnt += 1
            elif ( 0 < i < N-K ) and ( row[i-1] == 0 ) and ( row[i] == 1 ) and ( row[i:i+K] == [1]*K ) and ( row[i+K] == 0 ):
                cnt += 1
            elif ( i == 0 ) and ( row[i:i+K] == [1]*K ) and ( row[i+K] == 0 ):   
                cnt += 1

    # 전치
    for i in range(N):
        for j in range(N):
            if i < j:
                word_grid[i][j], word_grid[j][i] = word_grid[j][i], word_grid[i][j]

    # 열
    for col in word_grid:
        for j in range(N-K+1):
            if ( j == (N-K) ) and ( col[j-1] == 0 ) and ( col[j:] == [1]*K ):
                cnt += 1
            elif ( 0 < j < N-K ) and ( col[j-1] == 0 ) and ( col[j] == 1 ) and ( col[j:j+K] == [1]*K ) and ( col[j+K] == 0 ):
                cnt += 1
            elif ( j == 0 ) and ( col[j:j+K] == [1]*K ) and ( col[j+K] == 0 ):
                cnt += 1    

    print(f"#{tc} {cnt}")