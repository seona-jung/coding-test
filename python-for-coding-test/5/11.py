# 나
n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y, result):
    # 길을 벗어났다면
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 출구에 도달했다면
    if x == n - 1 and y == m - 1:
        result_list.append(result)
        # return True

    # 뚫린 길이고 방문하지 않은 길이라면
    if graph[x][y] == 1:
        graph[x][y] = result
        dfs(x - 1, y, result + 1)  # 상
        dfs(x + 1, y, result + 1)  # 하
        dfs(x, y - 1, result + 1)  # 좌
        dfs(x, y + 1, result + 1)  # 우

    # # 막힌 길이라면
    # return False

result = 1
result_list = []
dfs(0, 0, result)
# 출구까지 가는 경로가 여러 개라면 그중 최단 거리 반환
print(min(result_list))


# 저자
# from collections import deque
#
# # N, M을 공백을 기준으로 구분하여 입력 받기
# n, m = map(int, input().split())
# # 2차원 리스트의 맵 정보 입력 받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# # BFS 소스코드 구현
# def bfs(x, y):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque()
#     queue.append((x, y))
#
#     # []로 안 묶고 바로 이렇게 하면 오류 난다.
#     # queue = deque((x, y))
#     # deque 객체에 append로 넣을 때 비어 있었다면 알아서 맨 처음에 []로 묶어서 넣어준다.
#     # 그 다음에 append할 때마다는 처음에 생성했던 하나의 []안에 요소를 추가한다.
#
#     # 따라서 이렇게 하면 오류 안 난다.
#     # queue = deque([(x, y)])
#
#     # 큐가 빌 때까지 반복하기
#     while queue:
#         x, y = queue.popleft()
#         # 현재 위치에서 4가지 방향으로의 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 미로 찾기 공간을 벗어난 경우 무시
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             # 벽인 경우 무시
#             if graph[nx][ny] == 0:
#                 continue
#             # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#
#     # 가장 오른쪽 아래까지의 최단 거리 반환
#     return graph[n - 1][m - 1]
#
# # BFS를 수행한 결과 출력
# print(bfs(0, 0))