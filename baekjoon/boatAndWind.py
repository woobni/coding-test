n, s, r = map(int ,input().split())
broken = list(map(int, input().split()))
haveMore = list(map(int, input().split()))

boats = [1] * n

# 손상된 보트 -> 보유 보트수 -1
for i in broken:
    boats[i-1] -= 1

# 여분의 보트 -> 보유 보트수 +1
for i in haveMore:
    boats[i-1] += 1

for i in range(n):
    if boats[i] == 0: # 손상된 보트일 때(보트 보유수가 0)
        if i==0: # 첫 번째 순서
            if boats[i+1] == 2:
                boats[i+1] = 1
                boats[i] = 1

        elif i == n-1: # 마지막 순서
            if boats[i-1] == 2:
                boats[i-1] = 1
                boats[i] = 1

        else:
            if boats[i-1] == 2:
                boats[i-1] = 1
                boats[i] = 1
                continue              
            if boats[i+1] == 2:
                boats[i+1] = 1
                boats[i] = 1
                continue

    else: continue
    
print(boats.count(0))