import sys


sys.stdin = open('4865_LengthOfString.txt')

T = int(input())
for tc in range(1, T+1):
    ptn = input()
    string = input()

    my_dict = {}
    for alp in ptn:
        my_dict[alp] = 0
    
    for elem in string:
        if elem in ptn:
            my_dict[elem] += 1

    max_value = 0
    for value in my_dict.values():
        if value > max_value:
            max_value = value

    print(f"#{tc} {max_value}")