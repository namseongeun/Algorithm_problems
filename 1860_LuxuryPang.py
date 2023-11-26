import sys


sys.stdin = open('1860_LuxuryPang.txt')

T = int(input())
for tc in range(1, T+1):
    customers, time, bread = map(int, input().split())
    customers_arrive = sorted(list(map(int, input().split())))

    bread_array = [0] * (customers_arrive[-1] + 1)

    for i in range(time, len(bread_array), time):
        bread_array[i] += bread

    result = 'Possible'
    for arrive in customers_arrive:
        if sum(bread_array[:arrive + 1]) <= 0:
            result = 'Impossible'
            break
        else:
            bread_array[arrive] -= 1

    print(f'#{tc} {result}')