import sys
sys.stdin = open('1206_View.txt')

for tc in range(10):
    N = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    idx = 2

    while idx < N-2:
        if buildings[idx] == max(buildings[idx-2:idx+3]):
            result += buildings[idx] - max(buildings[idx - 2], buildings[idx - 1], buildings[idx + 1], buildings[idx + 2])
            idx += 3
        else:
            idx += 1

    print(f"#{tc} {result}")