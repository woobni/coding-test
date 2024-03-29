import sys

input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

# 현재 채널에서 + 혹은 - 만 사용하여 이동하는 경우
answer = abs(100 - target)

# 작은수에서 큰수로 이동할땐 500,000까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올 수도 있으므로 1,000,000까지 봐야함
for num in range(1000001):
    num = str(num)
    
    for j in range(len(num)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        # 하나라도 숫자가 고장났으면 숫자 버튼으로는 해당 숫자로 못 감
        if int(num[j]) in broken:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 answer 비교 후 업데이트
        elif j == len(num) - 1:
            # min(기존답, 해당 번호로부터 타겟까지의 차이 + 번호를 누른 횟수)
            answer = min(answer, abs(int(num) - target) + len(num))

print(answer)