import sys


sys.stdin = open('4466_MakeMaxGradeCard.txt')

def selectionSort(X):
    for i in range(len(X)-1):
        minIdx = i
        for j in range(i+1, len(X)):
            if X[minIdx] < X[j]:
                minIdx = j        
        X[i], X[minIdx] = X[minIdx], X[i]
    return X


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    all_scores = list(map(int, input().split()))

    sorted_scores = selectionSort(all_scores)

    upper_scores = sorted_scores[:K]

    total_max = 0
    for upper_score in upper_scores:
        total_max += upper_score

    print(f'#{tc} {total_max}')