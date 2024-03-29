# 쩰리가 오른쪽, 아래쪽으로만 이동할 수 있기 때문에 방향벡터를 두 개 만들어놓고 BFS를 수행

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        if (x, y) == (n - 1, n - 1):
            return 1
        for i in range(2):
            nx = x + dx[i] * graph[x][y]
            ny = y + dy[i] * graph[x][y]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
    return 0

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [0, 1]
dy = [1, 0]
print("HaruHaru" if bfs(0, 0) else "Hing")