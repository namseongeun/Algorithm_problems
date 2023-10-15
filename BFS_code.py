graph = {}

def BFS(start_node):
    visited = []
    queue = [start_node]

    while queue:
        tmp = queue.pop(0)
        if tmp not in visited:
            visited.append(tmp)
            for node in graph[tmp]:
                if node not in visited:
                    queue.append(node)