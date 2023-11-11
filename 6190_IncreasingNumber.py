import sys


sys.stdin = open('IncreasingNumber.txt')

def is_dango(x):
    x = str(x)
    for i in range(len(x)-1):
        if int(x[i]) > int(x[i+1]):
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    danjo_num = -1
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            number = A[i] * A[j]
            if (is_dango(number) == True) and (number > danjo_num):
                danjo_num = number

    print(f"#{tc} {danjo_num}")
    