import sys


sys.stdin = open('4861_Palindrome.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    word_grid = [list(input()) for _ in range(N)]

    # 행
    for row in word_grid:
        for i in range(N-M+1):
            string = row[i:i+M]
            if string == string[::-1]:
                palindrome = string
                break

    # 전치
    for i in range(N):
        for j in range(N):
            if i < j:
                word_grid[i][j], word_grid[j][i] = word_grid[j][i], word_grid[i][j]

    # 열
    for col in word_grid:
        for j in range(N-M+1):
            string = col[j:j+M]
            if string == string[::-1]:
                palindrome = string
                break

    # 회문이 리스트 형태이므로 최종 결과를 문자열 형태로 변환
    result = ''.join(palindrome)

    print(f'#{tc} {result}')