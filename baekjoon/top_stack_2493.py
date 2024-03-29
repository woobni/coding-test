# 스택을 오른쪽으로 눕혀서 생각 (왼쪽이 닫힘)
# 가장 먼저 만나는 높이가 같거나 큰 탑에서 수신 가능
# 가장 먼저 만나는 탑이 높이가 작다면 스택에서 비움 -> 신경쓰지 않아도 되기 때문 
# 왜냐하면, 그 뒤에 들어오는 현재 탑의 전파보다 작은 모든 전파는 현재 탑에서 수신 가능

N = int(input())
tops = list(map(int, input().split()))

stack = []
answer = []
for i in range(N):
    while stack:
        if stack[-1][1] > tops[i]: # 수신 가능한 상황
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()

    if not stack: # 스택이 비면 수신할 탑이 없음
        answer.append(0)

    stack.append((i, tops[i]))

print(*answer)