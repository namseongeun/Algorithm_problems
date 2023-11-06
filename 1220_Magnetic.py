import sys


sys.stdin = open('1220_Magnetic.txt')

for tc in range(1, 11):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(100)]

    # 전치
    for i in range(100):
        for j in range(100):
            if i > j:
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

    # 0 제외시키기
    new_grid = []
    for row in grid:
        new_row = []
        for elem in row:
            if elem != 0 :
                new_row.append(elem)
        new_grid.append(new_row)

    # 패턴 [1,2]: 교착상태
    glue = 0
    for n_row in new_grid:
        for i in range(len(n_row) - 1):
            if n_row[i:i+2] == [1,2]:
                glue += 1

    print(f"#{tc} {glue}")