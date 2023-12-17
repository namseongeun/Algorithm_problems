import sys


sys.stdin = open('4874_Forth.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(input().split())

    num_arr = []
    symbol_arr = []
    symbols = ['+', '-', '*', '/']

    for elem in arr:
        if elem in symbols:
            symbol_arr.append(elem)
        elif elem != '.':
            num_arr.append(elem)
    

    if ( len(num_arr) - 1 ) != len(symbol_arr):
        result = 'error'

    elif ( len(num_arr) - 1 ) == len(symbol_arr):

        while len(num_arr) != 1:

            if len(num_arr) == 1:            
                answer = num_arr[0]
                break

            else:   
                A = int(num_arr.pop(0))
                B = int(num_arr.pop(0))

                symbol = symbol_arr.pop(0)

                if symbol == '+':
                    C = A + B
                    num_arr.append(C)
                elif symbol == '-':
                    C = A - B
                    num_arr.append(C)
                elif symbol == '*':
                    C = A * B
                    num_arr.append(C)                
                else:
                    C = A / B
                    num_arr.append(C)                

    print(answer)
