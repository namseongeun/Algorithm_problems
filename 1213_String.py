import sys


sys.stdin = open('1213_String.txt', encoding='utf8')

for _ in range(10):
    tc = input()
    check_str = input()
    total_str = input()


    n, N = len(check_str), len(total_str)

    cnt = 0
    for i in range(N - n + 1):
        if total_str[i: i+n] == check_str:
            cnt += 1
            i + n
        else:
            i + n

    print(f"#{tc} {cnt}")