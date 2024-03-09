import sys


sys.stdin = open('1231_InorderSearch.txt')

# 노드 딕셔너리에서 각 키에 해당하는 값을 중위 탐색 순서로 출력하는 함수
def in_order(V):        
    if V:
        in_order(left_children[V])
        print(nodes[V], end="")
        in_order(right_children[V])


for tc in range(1, 11):
    N = int(input())
    nodes = {}          # 노드의 번호를 키, 그 값을 값으로 가지는 딕셔너리
    left_children = [0] * (N+1)   # 각 인덱스 번호에 해당하는 부모노드의 왼쪽 자식노드를 나타내는 리스트
    right_children = [0] * (N+1)   # 각 인덱스 번호에 해당하는 부모노드의 오른쪽 자식노드를 나타내는 리스트

    for _ in range(N):
        p_c = list(input().split())
        
        if len(p_c) == 4:           # 만약 입력 받은 리스트 길이가 4라면,
            p_node = int(p_c[0])    # 첫 번째 요소: 부모노드의 번호
            node_val = p_c[1]       # 두 번째 요소: 부모노드의 값
            c1_node = int(p_c[2])   # 세 번째 요소: 왼쪽 자식노드의 번호
            c2_node = int(p_c[3])   # 네 번째 요소: 오른쪽 자식노드의 번호
            
            nodes[p_node] = node_val    # 노드 딕셔너리에 키와 값 넣기
            left_children[p_node] = c1_node       # 왼쪽 자식노드 리스트에 값 넣기
            right_children[p_node] = c2_node       # 오른쪽 자식노드 리스트에 값 넣기

        elif len(p_c) == 3:         # 만약 입력 받은 리스트 길이가 3이라면,
            p_node = int(p_c[0])    # 첫 번째 요소: 부모노드의 번호
            node_val = p_c[1]       # 두 번째 요소: 부모노드의 값
            c1_node = int(p_c[2])   # 세 번째 요소: 왼쪽 자식노드의 번호
            
            nodes[p_node] = node_val    # 노드 딕셔너리에 키와 값 넣기
            left_children[p_node] = c1_node       # 왼쪽 자식노드 리스트에 값 넣기

        elif len(p_c) == 2:         # 만약 입력 받은 리스트 길이가 2라면,
            p_node = int(p_c[0])    # 첫 번째 요소: 부모노드의 번호
            node_val = p_c[1]       # 두 번째 요소: 부모노드의 값    
            
            nodes[p_node] = node_val    # 노드 딕셔너리에 키와 값 넣기

    # 형식에 맞게 출력하기
    print(f"#{tc}", end=" ")
    in_order(1)
    print()