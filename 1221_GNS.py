import sys


sys.stdin = open('1221_GNS.txt')

T = int(input())
for _ in range(T):
    tc, N = input().split()
    nums = list(input().split())
    
    num_lst = ["ZRO","ONE","TWO","THR","FOR","FIV","SIX","SVN","EGT","NIN"]
    cnt_lst = [0] * 10

    for num in nums:
        for i in range(10):
            if num == num_lst[i]:
                cnt_lst[i] += 1

    print(tc)
    for i in range(10):
        for _ in range(cnt_lst[i]):
            print(num_lst[i], end=" ")