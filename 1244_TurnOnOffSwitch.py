import sys


sys.stdin = open('1244_TurnOnOffSwitch.txt')

S = int(input())
switches = list(map(int, input().split()))
students = int(input())

for _ in range(students):
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(len(switches)):
            if (switches[i] == 0) and ((i+1) % num == 0) and ((i+1) >= num):
                switches[i] = 1
            elif (switches[i] == 1) and ((i+1) % num == 0) and ((i+1) >= num):
                switches[i] = 0

    # else:
    #     N = num - 1
    #     while True:
    #         cnt = 0
    #         if ((N - (cnt + 1)) < 0) or ((N + (cnt+1)) >= len(switches)):
    #             for switch in switches[N - cnt : N + (cnt + 1)]:
    #                 if switch == 0:
    #                     switch = 1
    #                 else:
    #                     switch = 0
                
    #             break

    #         elif (switches[N - (cnt + 1)] != switches[N + (cnt+1)]):
    #             for switch in switches[N - cnt : N + (cnt + 1)]:
    #                 if switch == 0:
    #                     switch = 1
    #                 else:
    #                     switch = 0
                
    #             break
            
    #         else:
    #             cnt += 1

    else:
        for n in range(1, num+1):
            if (num-1) - n < 0 or (num+1) - n > len(switches)-1:
                if switches[(num-1)] == 0:
                    switches[(num-1)] = 1
                    break
                else:
                    switches[(num-1)] = 0
                    break
            elif switches[(num-1) - n] == switches[(num-1) + n] == 1:
                switches[(num-1) - n] = switches[(num-1) + n] = 0
            elif switches[(num-1) - n] == switches[(num-1) + n] == 0:
                switches[(num-1)-n] = switches[(num-1)+n] = 1
            else:
                if switches[(num-1)] == 0:
                    switches[(num-1)] = 1
                    break
                else:
                    switches[(num-1)] = 0
                    break


    print(switches)