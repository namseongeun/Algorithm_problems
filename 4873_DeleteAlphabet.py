import sys


sys.stdin = open('4873_DeleteAlphabet.txt')

T = int(input())
for tc in range(1, T+1):
    text = list(input())

    # 인덱스 초기설정
    idx = 0

    while len(text) >= 2:
        if text[idx] == text[idx+1]:
            text.pop(idx)
            text.pop(idx)
            idx = 0

        else:
            idx += 1

            if idx == len(text) - 1:
                break
    
    print(f"#{tc} {len(text)}")
