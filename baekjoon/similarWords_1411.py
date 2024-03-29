# 단어들 중 두 개씩 선택하여 각각의 음절을 모두 비교하고자 함 -> 삼중 for-loop
# 두 개의 다른 알파벳을 하나의 알파벳으로 바꿀 수 없다는 조건을 체크하기 위해,
# 두 개의 각 단어와 매핑 되는 두 개의 리스트가 필요할듯(방문 처리). 리스트 크기는 알파벳 개수

import sys

input=sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)] # N: 0 ~ N-1, strip() : \n 제거

cnt = 0
for i in range(N-1): # i: 0 ~ N-2
    for j in range(i+1, N): # j : i+1 ~ N-1 
        word_1 = words[i]
        word_2 = words[j]

        flag = True

        visited_1 = [0] * (ord('z') - ord('a') + 1)
        visited_2 = [0] * (ord('z') - ord('a') + 1)

        for k in range(len(word_1)):
            idx_1 = ord(word_1[k]) - ord('a') # idx: 0~25
            idx_2 = ord(word_2[k]) - ord('a') # idx: 0~25

            if not visited_1[idx_1] and not visited_2[idx_2]:
                # visited[idx] = 1 로 하면 문자 비교가 안됨
                visited_1[idx_1] = word_2[k]
                visited_2[idx_2] = word_1[k]

            elif word_1[k] != visited_2[idx_2]:
                flag = False
                break
            
        if flag:
            cnt += 1

print(cnt)