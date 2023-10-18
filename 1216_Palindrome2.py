import sys


sys.stdin = open('1216_Palindrome2.txt')

for _ in range(10):
    tc = input()
    grid = [list(input()) for _ in range(100)]

    max_len = 0

    # 행
    for row in grid:
        ptn_len = 1
        while ptn_len <= 100:
            for n in range(100 - ptn_len + 1):
                if ( row[n:n + ptn_len] == row[n:n + ptn_len][::-1] ) and ( ptn_len > max_len ):
                    max_len = ptn_len
            
            ptn_len += 1

    # 전치
        for i in range(100):
            for j in range(100):
                if i < j:
                    grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
                    
    # 열
    for col in grid:
        ptn_len = 1
        while ptn_len <= 100:
            for n in range(100 - ptn_len + 1):
                if col[n:n + ptn_len] == col[n:n + ptn_len][::-1]:
                    if ptn_len > max_len:
                        max_len = ptn_len
            ptn_len += 1

    print(f"#{tc} {max_len}")