import sys


sys.stdin = open('4837_SumOfSubsets.txt')

T = int(input())
for tc in range(1, T+1):
    A = list(range(1, 12))
    N, K = map(int, input().split())

    all_subsets = []
    for i in range(1 << 12):
        each_subset = []
        for j in range(11):
            if i & (1 << j):
                each_subset.append(A[j])
            
        if each_subset not in all_subsets:
            all_subsets.append(each_subset)

    zero_sum_subsets = []
    for each_subset in all_subsets:
        if len(each_subset) == N and sum(each_subset) == K:
            zero_sum_subsets.append(each_subset)
    
    cnt = 0    
    for zero_sum_subset in zero_sum_subsets:
        cnt += 1

    print(f"#{tc} {cnt}")
