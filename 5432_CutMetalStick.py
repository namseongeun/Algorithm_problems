import sys


sys.stdin = open('5432_CutMetalStick.txt')

T = int(input())
for tc in range(1, T+1):
    S = input()
    cnt = stick = 0

    for i in range(len(S)):
        if S[i] == '(':
            # 여는 괄호 다음에 바로 닫는 괄호가 나오면 레이저이니까 자른다.
            # 횟수는 현재 막대의 길이와 같다.
            if S[i+1] == ')':
                cnt += stick
            # 아니라면, 쇠막대가 증가하는 것이므로 막대의 갯수를 늘려준다.
            else:
                stick += 1
        
        else:
            if S[i-1] == ')':
                cnt += 1
                stick -= 1

            # 여는 괄호가 전에 나왔다면 레이저의 끝
            # 하지만 위에서 이미 더해줬으니까 여기서는 따로 더하지 않는다.

    print(f'#{tc} {cnt}')
