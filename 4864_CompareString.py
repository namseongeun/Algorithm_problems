import sys


sys.stdin = open('4864_CompareString.txt')

T = int(input())
for tc in range(1, T+1):
    ptn = input()
    string = input()
    n = len(ptn)
    N = len(string)

    for i in range(N-n+1):
        if string[i: i+len(ptn)]  == ptn:
            result = 1
            break
        result = 0

    print(f'#{tc} {result}')