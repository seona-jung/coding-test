from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


visited = [False] * 9

def bfs(start):
    # queue = deque()
    # queue.append(start)
    queue = deque([start])
    visited[start] = True
    # print(start, end=' ')

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for adjacent_node in graph[node]:
            if not visited[adjacent_node]:
                queue.append(adjacent_node)
                visited[adjacent_node] = True
                # print(adjacent_node, end=' ')


bfs(1)
