graph = {}

def DFS(start_node):
    visited = []
    stack = [start_node]

    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.append(tmp)
            for node in graph[tmp][::1]:
                if node not in visited:
                    stack.append(node)