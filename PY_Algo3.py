def B():
    try:
        A = input('0~100사이의 점수를 입력하세요')
        if 0 <= int(A) <= 100:
            A = int(A)
        else:
            B()
    except:
        B()

    return A


i = 1
j = 2
k = 's'
o = 'sksksk'
l = [1, 2, 3, 4]
m = [4, 5 ,6]
n = [4]


print(m * 3)
