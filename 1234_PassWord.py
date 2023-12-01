import sys


sys.stdin = open('1234_PassWord.txt')

for tc in range(1, 11):
    N, password = input().split()
    password = list(password)

    i = 0 
    while len(password) >= 2:
        if password[i] == password[i+1]:
            password.pop(i)
            password.pop(i)
            i = 0

        else:
            i += 1
            if i == len(password) - 1:
                break
    
    password = ''.join(password)

    print(f'#{tc} {password}')