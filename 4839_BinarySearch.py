import sys


sys.stdin = open('4839_BinarySearch.txt')

T = int(input())
for tc in range(1, T+1):
    P, p_a, p_b = map(int, input().split())

    book = list(range(1, P+1))

    cnt_a = 0
    cnt_b = 0

    start = 0
    end = P-1
    while start <= end:
        middle = (start + end) // 2

        if book[middle] == p_a:
            cnt_a += 1
            break
        elif book[middle] > p_a:
            cnt_a += 1
            end = middle
        else:
            cnt_a += 1
            start = middle

    start = 0
    end = P - 1
    while start <= end:
        middle = (start + end) // 2
        if book[middle] == p_b:
            cnt_b += 1
            break
        elif book[middle] > p_b:
            cnt_b += 1
            end = middle
        else:
            cnt_b += 1
            start = middle

    if cnt_a == cnt_b:
        result = 0
    elif cnt_a > cnt_b:
        result = "B"
    elif cnt_b > cnt_a:
        result = "A"

    print(f"#{tc} {result}")