# 항상 생각할 것
# 0~n-1 x 0~m-1
# 행 수가 x축(n)(밑으로 증가), 열 수가 y축(m)(오른쪽으로 증가)

# n, m 입력 받기 -> n*m 얼음 틀
n, m = map(int, input().split())

# 얼음 틀 구멍(0), 칸막이(1) 입력받아서 채워 넣기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 모두 재귀적으로 호출
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우
        return True
    # 막힌 틀(1)이라면
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
