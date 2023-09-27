import sys


sys.stdin = open('1208_Flatten.txt')

for tc in range(1, 11):
    N = int(input())
    box_piles = list(map(int, input().split()))

    while True:
        max_boxes = max(box_piles)
        min_boxes = min(box_piles)

        if (max_boxes - min_boxes) <= 1 or N == 0:
            result = max_boxes - min_boxes
            break

        else:
            N -= 1
            box_piles.remove(max_boxes)
            box_piles.remove(min_boxes)
            box_piles.extend((max_boxes - 1, min_boxes + 1))

    print(f"#{tc} {result}")