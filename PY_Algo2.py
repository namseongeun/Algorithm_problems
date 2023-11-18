A = 'OXXOOXXXOOOXO'

N = len(A)

total_score = 0
tmp_score = 1

for i in range(N):
    if i == 0:
        if A[i] == 'O':
            total_score += 1
            tmp_score += 1
    else:
        if A[i] == 'O':
            total_score += tmp_score
            tmp_score += 1
        else:
            tmp_score = 1

print(total_score)