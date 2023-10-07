import sys


sys.stdin = open('1859_Millionare_Pjt.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    dp = [0] * N

    max_price = prices[-1]
    for i in range(N-2, -1, -1):
        if max_price > prices[i]:
            dp[i+1] = max_price - prices[i]
        else:
            max_price = prices[i]

    print(f"#{tc} {sum(dp)}")