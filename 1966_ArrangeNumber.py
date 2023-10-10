import sys


sys.stdin = open('1966_ArrangeNumber.txt')

# for문을 제외한 내장함수 쓰지 않는 풀이

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    length = 0
    for _ in nums:
        length += 1

    for i in range(length):
        for j in range(length):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
        
    print(f'#{tc}', end=' ')
    print(*nums)