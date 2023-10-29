import sys


sys.stdin = open('3143_FastestTyping.txt')

T = int(input())
for tc in range(1, T+1):
    string, ptn = list(input().split())
    N, M = map(len, (string, ptn))

    typing = 0
    i = 0

    while i < N:
        if string[i:i+M] == ptn:
            typing += 1
            i += M
        
        else:
            typing += 1
            i += 1

    print(f'#{tc} {typing}')