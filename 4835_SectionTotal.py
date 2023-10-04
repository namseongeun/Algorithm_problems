import sys 


sys.stdin = open('4835_SectionTotal.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums  = list(map(int, input().split()))

    section_total_list = []
    for i in range(N-M+1):
        section_nums = nums[i:i+M]
        section_total = 0
        for section_num in section_nums:
            section_total += section_num
        section_total_list.append(section_total)


    max_total = section_total_list[0]
    min_total = section_total_list[0]
    section_total_cnt = 0

    for section_total in section_total_list:
        section_total_cnt += 1

    for n in range(section_total_cnt):
        if max_total < section_total_list[n]:
            max_total = section_total_list[n]
        if min_total > section_total_list[n]:
            min_total = section_total_list[n]

    result = max_total - min_total

    print(f"#{tc} {result}")
