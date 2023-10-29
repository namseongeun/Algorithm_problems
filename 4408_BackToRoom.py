import sys


sys.stdin = open('4408_BackToRoom.txt')

total_room = []
for i in range(1, 401, 2):
    total_room.append([i, i+1])

T = int(input())
for tc in range(1, T+1):
    movement_lines = [0] * 200

    students = int(input())
    for student in range(students):
        tmp, togo = map(int, input().split())
        if tmp <= togo:
            for i in range((tmp-1)//2, (togo+1)//2):
                movement_lines[i] += 1
        else:
            for j in range((togo-1)//2, (tmp+1)//2):
                movement_lines[j] += 1
    
    max_movement = 1
    for movement_line in movement_lines:
        if movement_line > max_movement:
            max_movement = movement_line

    print(f'#{tc} {max_movement}')