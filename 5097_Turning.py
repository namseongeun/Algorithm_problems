import sys


sys.stdin = open('5097_Turning.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    for _ in range(M):
        first_num = nums.pop(0)
        nums.append(first_num)

    print(f"#{tc} {nums[0]}")