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

