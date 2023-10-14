import sys


sys.stdin = open('5356_SayVertical.txt')

T = int(input())
for tc  in range(1, T+1):
    str_mat = [[''] * 15 for _ in range(15)]
    for i in range(5):
        string = list(input())
        l = len(string)
        str_mat[i][0:l] = string[:]

    result_str = ""

    for i in range(15):
        for j in range(15):
            if str_mat[j][i] != '':
                result_str += str_mat[j][i]

    print(f"#{tc} {result_str}")