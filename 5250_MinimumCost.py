import sys


sys.stdin = open('5250_MinimumCost.txt')


def BFS(si, sj):
    # 단순하게 거리를 구하는게 아닌 이동비용의 최소값을 반환하는 문제
    # 해당 지역까지의 가능한 최대값(높이 최대값: 1000 이동거리 최대값: 10000)으로
    # 문제에서 주어진 지역격자와 같은 크기의 이동비용 격자를 생성한다.
    cost_grid = [[5010000]*N for _ in range(N)]
    # 단, 시작점은 에너지가 전혀 들지 않으므로 해당 비용값을 0으로 초기화한다.
    cost_grid[si][sj] = 0

    # 큐에 시작점 좌표를 넣는다.
    queue = [[si, sj]]

    # 큐가 비어있는 동안 반복
    while queue:
        [ti, tj] = queue.pop(0)             # 큐에서 가장 왼쪽의 요소를 꺼내,
        for d in range(4):                  # 상하좌우의 좌표 중에 범위 내 요소들에 대하여,
            ni = ti + di[d]
            nj = tj + dj[d]
            if 0 <= ni < N and 0 <= nj < N:

    # 1. 이동비용 구하기 ------------------------------------------------------------------
                # 만약 더 높은 지역으로 이동하려면 기본 비용 1과 높이 차만큼의 추가 비용이 든다.
                if grid[ni][nj] > grid[ti][tj]:
                    cost = grid[ni][nj] - grid[ti][tj] + 1
                # 그렇지 않은 경우에는 기본 비용 1만큼만 든다.
                else:
                    cost = 1

    # 2. 비용격자의 특정 지역에 대해 가능한 최소 이동비용으로 갱신하기 --------------------------            
                # 만약에 현재까지 구한 [ni,nj]지역으로 이동하기까지의 최소비용이,
                # 방금 구한 최소비용보다 크면 갱신하고 그 지역을 큐에 더한다.
                if cost_grid[ti][tj] + cost < cost_grid[ni][nj]:
                    cost_grid[ni][nj] = cost_grid[ti][tj] + cost
                    queue.append([ni, nj])

    # 3. BFS 순회가 종료되면 도착점까지 든 최소 이동비용을 반환 -------------------------------
    return cost_grid[ei][ej]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 델타 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 도착지점의 좌표
    ei = ej = N-1
    # BFS에 시작좌표를 넣어서 도착점까지의 최소 비용을 구한다.
    result = BFS(0, 0)
    # 형식에 맞게 출력
    print(f"#{tc} {result}")
