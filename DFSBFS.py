'''
#dfs - 깊이우선 - 재귀함수(stack)으로 구현
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#bfs - 너비우선 - queue로 구현
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]
]
visited = [False] * 9
dfs(graph, 1, visited)
print()
visited = [False] * 9
bfs(graph, 1, visited)
'''

'''
#입력
n, m = [int(i) for i in input().split()]
map = []
for i in range(n):
    map.append([i for i in input()])

#구현

answer = 0

visited = [[False if i=="0" else True for i in j] for j in map]

start = (0,0)
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            start = (i, j)


def dfs(start):
    global answer
    if not (0 <= start[0] <= n-1 and 0<= start[1] <= m-1): #index error
        return False
    if visited[start[0]][start[1]]:
        return False
    visited[start[0]][start[1]] = True
    while True:
        dfs((start[0] - 1, start[1]))
        dfs((start[0] + 1, start[1]))
        dfs((start[0], start[1] - 1))
        dfs((start[0], start[1] + 1))
        return True

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            #print(i,j)
            if dfs((i,j)):
                answer += 1

print(answer)
''' # 음료수 얼려 먹기
'''
from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append([1 if i == '1' else 0 for i in input()])


dir = [[1,0],[0,1],[0,-1],[-1,0]]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        can_go = [(x + d[0], y + d[1]) for d in dir if
                  0 <= x + d[0] <= n - 1 and 0 <= y + d[1] <= m - 1]  # 갈 수있는 방향 리스트
        for nx, ny in can_go:
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))
''' #미로찾기
