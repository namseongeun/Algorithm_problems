import sys


sys.stdin = open('1110_PlusCycle.txt')

original_num = int(input())

cycle_cnt = 0

cnt_num = original_num

if cnt_num < 10:
    cnt_num *= 10

while True:
    if (cnt_num == original_num) and cycle_cnt != 0:
        break
    else:
        cnt_num = ((cnt_num % 10) * 10) + (((cnt_num // 10) + (cnt_num % 10)) % 10)
        cycle_cnt += 1

print(cycle_cnt)