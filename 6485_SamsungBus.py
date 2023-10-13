import sys


sys.stdin = open('6485_SamsungBus.txt')

T = int(input())
for tc in range(1, T+1):
    # N개의 노선을 시작 정류장과 끝 정류장을 묶어 리스트에추가
    N = int(input())
    lst_n = []
    for _ in range(N):
        A, B = map(int, input().split())
        lst_n.append([A, B])

    # P개의 정류장을 입력받은 뒤 각 정류장이 앞서 주어진 N개의 노선 중 포함된 경우에는 그 수를 세어 리스트로 만든다.
    # 즉 최종 리스트는 P개의 정류장들이 각각 포함된 노선 개수를 나타낸다.
    P = int(input())
    result_lst = [0] * P
    for p in range(P):
        C = int(input())
        for n in range(N):
            if lst_n[n][0] <= C <= lst_n[n][1]:
                result_lst[p] += 1

    # 형식에 맞게 출력한다.
    print(f'#{tc}', end=' ')
    print(*result_lst)
