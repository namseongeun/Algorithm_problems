import sys
import copy


sys.stdin = open('1211_Ladder_2.txt')

for _ in range(10):
    tc = int(input())
    ladder_mat = [list(map(int, input().split())) for _ in range(100)]
    
    start_idxes = []
    for n in range(100):
        if ladder_mat[0][n] == 1:
            start_idxes.append(n)

    min_cnt = 10000
    min_idx = 100

    for start_idx in start_idxes:
        copied_mat = copy.deepcopy(ladder_mat)
        i = 0
        j = start_idx
        cnt = 0

        while i <= 99:
            if cnt >= min_cnt:
                cnt = 10000
                break
            # 좌로
            if 0 <= (j-1) < 100 and copied_mat[i][j-1] == 1:
                copied_mat[i][j] = 0
                j -= 1
                cnt += 1
            # 우로
            elif 0 <= (j+1) < 100 and copied_mat[i][j+1] == 1:
                copied_mat[i][j] = 0
                j += 1
                cnt += 1
            # 아래로
            else:
                copied_mat[i][j] = 0
                i += 1
                cnt += 1

        if cnt < min_cnt:
            min_cnt = cnt
            min_idx = start_idx

    print(f"#{tc} {min_idx}")