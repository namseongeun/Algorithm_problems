import sys


sys.stdin = open('4874_Forth.txt')

T = int(input())
for tc in range(1, T+1):
    str_lst = list(input().split())[:-1]

    stack = []
    for char in str_lst:
        try:
            if char not in "*/+-":
                stack.append(int(char))
            else:
                x = stack.pop()     # 스택에서 가장 위에 있던거 (부호전에 있던 숫자중 뒷 숫자)
                y = stack.pop()     # 스택에서 그 다음 위에 있던거 (부호전에 있던 숫자중 앞 숫자)

                # 부호가 등장하면 그에 따라서 그 앞에 있는 숫자들을 조작
                if char == "+":
                    stack.append(y + x)
                elif char == "-":
                    stack.append(y - x)
                elif char == "*":
                    stack.append(y * x)
                elif char == "/":
                    stack.append(y // x)
        except:
            result = "error"
            break

    if len(stack) != 1:
        result = "error"
    else:
        result = stack[0]

    print(f'#{tc} {result}')