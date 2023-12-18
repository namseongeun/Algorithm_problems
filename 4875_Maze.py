import sys


sys.stdin = open('4875_Maze.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]

    # 델타: 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 그래프를 위해 딕셔너리 생성
    # 벽을 제외한 출구, 입구, 길 노드의 좌표를 모두 딕셔너리의 키로 생성합니다.
    my_dict = {}
    for i in range(N):
        for j in range(N):
            if maze[i][j] != 1:
                my_dict[(i, j)] = []
    
    # 각 키 노드에 연결된 노드들의 좌표를 밸류로 집어 넣습니다.
    for (k, l) in my_dict:
        for d in range(4):
            if 0 <= k + di[d] < N and 0 <= l + dj[d] < N and maze[k+di[d]][l+dj[d]] != 1:
                my_dict[(k, l)].append((k+di[d], l+dj[d]))

    # 시작 노드의 좌표를 찾습니다.
    for (a, b) in my_dict.keys():
        if maze[a][b] == 2:
            start_node = (a, b)

    # 지나간 길을 기록할 리스트와 돌아갈 길을 기록할 스택을 생성하고 스택에는 시작 노드의 좌표를 넣습니다.
    # 미로에 들어서는 순간 출구는 곧 지난 길에 속하기 때문입니다.
    discovered = []
    stack = [start_node]

    # 결과의 기본값은 0입니다. 길을 따라 출구로 나갈 수 있을 때만 1이 결과가 됩니다.
    result = 0
    
    # 모든 벽을 제외한 길을 다 가보면 반복을 종료합니다.
    while len(discovered) != len(my_dict):
    
    # 스택에 기록된 지금까지 온 길을 보며 그 길이 아직 방문기록에 없다면 추가하고
    # 그래프 딕셔너리에서 그 길(노드)와 연결된 모든 길(노드)를 스택에 추가합니다.
    # 그런데 중간에 연결된 노드의 값이 출구이면 나갈 수 있다는 뜻이므로 결과를 1로하고 반복문을 조기 종료합니다.
        try:
            (v, w) = stack.pop()
            if (v, w) not in discovered:
                discovered.append((v, w))
                for (x, y) in my_dict[(v, w)]:
                    if maze[x][y] == 3:
                        result = 1
                        break
                    else:
                        stack.append((x, y))
    
    # 만약 스택에 기록해둔 돌아갈 길이 더이상 없으면 종료합니다.
        except:
            break
            
    print(f"#{tc} {result}")