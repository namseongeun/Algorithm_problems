import sys


sys.stdin = open('4846_MinMax.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    min_num = numbers[0]
    max_num = numbers[0]

    for n in range(N):
        if min_num > numbers[n]:
            min_num = numbers[n]
        elif max_num < numbers[n]:
            max_num = numbers[n]

    result = max_num - min_num

    print(f"#{tc} {result}")