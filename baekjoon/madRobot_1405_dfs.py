# 이동 경로 -> 좌표 -> 이차원 리스트, 방향 정의 필요
# 이동 경로가 단순하다는 것은 한 번 간 곳을 다시 가지 않는다는 것 
# 단순할 확률 = 한 번 간 곳을 다시 가지 않을 확률 -> 방문 처리 하며 DFS 탐색

from typing import List
import sys

# sys.setrecursionlimit(10**6) 
# 왜 여기서는 안해줘도 에러가 안나지? 저번 문제하고 무슨 차이?
# 저번 문제는 재귀 기본 제한을 늘려준 것. 이번 문제는 늘릴 필요가 없는 것

input=sys.stdin.readline

N,e,w,s,n = map(int, input().split())

# 가로 x축, 세로 y축 일 때
# 동,서,남,북 방향 정의 
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 동,서,남,북 이동할 확률
pred_list = [e,w,s,n]

# 현재 위치에서 최대 N만큼 이동해야 하므로 
# N이 중앙으로 오도록 2차원 배열 생성
graph = [[0]*(2*N+1) for _ in range(2*N+1)]

answer = 0

def dfs(x: int, y: int, pred: float, cnt: int):
    global answer

    if cnt == N:
        # cnt가 N인 모든 경우에 대한 OR 연산이므로 +
        answer += pred
        return

    # 현재 노드 방문 처리
    graph[x][y] = 1
    # 현재 노드의 방문 확률
    now_pred = pred
    
    for i in range(len(pred_list)):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < (2*N+1) and 0 <= next_y < (2*N+1):
            if not graph[next_x][next_y]:
                # 현재 위치에서 연달아 동서남북 이동할 경우에 대한 AND 연산이므로 *
                dfs(next_x, next_y, now_pred * (pred_list[i]/100), cnt+1)

                # 이후 실행될 dfs 함수 처리를 위해 방문 처리 해제
                graph[next_x][next_y] = 0

            else: 
                continue

dfs(N, N, 1, 0)

print(answer)