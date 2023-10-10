import sys


sys.stdin = open('4843_SpecialArrange.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    result = []
    for _ in range(5):
        result.extend((max(nums), min(nums)))
        nums.remove(min(nums))
        nums.remove(max(nums))

    print(f"#{tc}", end = " ")
    print(*result)