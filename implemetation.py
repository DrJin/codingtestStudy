#예제
'''
n = int(input())
directions = list(input().split())
index = [1,1]

for d in directions:
    if d == 'L':
        index[1] -= 1
    elif d == 'R':
        index[1] += 1
    elif d == 'U':
        index[0] -= 1
    elif d == 'D':
        index[0] += 1
    else:
        pass

    if index[0] < 1:
        index[0] = 1
    elif index[0] > n-1:
        index[0] = n-1
    elif index[1] < 1:
        index[1] = 1
    elif index[1] > n-1:
        index[1] = n-1

print(index)
''' #상하좌우
'''
n = int(input())

sec = (n+1)*60*60
result = 0

for t in range(sec):

    time = t//(60*60)
    min = (t - time*3600) // 60
    sec = (t - time*3600 - min* 60) % 60
    #print(str(time)+str(min)+str(sec))
    if "3" in str(time)+str(min)+str(sec):
        #print(time, min, sec)
        result += 1

print(result)
''' # 3이 들어간 시각
#실전문제
'''
def check_index(index):
    if index[0] < 0 or index[0] > 7 or index[1] < 0 or index[1] > 7:
        return False
    else:
        return True

index = input()
col, row = index[0], int(index[1])

#preprocessing
cols = ['a','b','c','d','e','f','g','h']
col = cols.index(col)
row -= 1
index = [col, row]
result = 0
steps = [[-2, -1],[-2, 1],[-1, 2],[1, 2],[2, 1],[2, -1],[1, -2],[-1, -2]]

for step in steps:
    if check_index([index[0]+step[0], index[1]+step[1]]):
        result += 1

print(result)
''' # 체스 기사 문제
'''
n, m = [int(i) for i in input().split()]
nx, ny, d = [int(i) for i in input().split()]
pos = [nx, ny] #현위치
map = []
have_to_go = 0 #have to go field #

for i in range(n):
    map.append([int(j) for j in input().split()])
    have_to_go += map[i].count(0)

result = 0
directions = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}
try_pos = 0 # 4 방향 검사
end_flag = False

map[pos[0]][pos[1]] = 2 # 시작점은 방문 완료
result += 1

while result != have_to_go:
    pos_to_go = pos
    map_to_go = 1
    while map_to_go in [1,2]: #갈 수 없으면
        pos_to_go = [pos[0] + directions[d][0], pos[1] + directions[d][1]]
        map_to_go = map[pos_to_go[0]][pos_to_go[1]]
        #print(pos, d, pos_to_go)
        d = (d+1)%4 # 위치 바꾸기
        try_pos += 1
        if try_pos != 4:
            continue
        else: #4방향을 다 가봐도 갈 수 있는 길이
            backward = map[pos[0]-directions[d][0]][pos[1]-directions[d][1]]
            if backward == 2: #가본곳이면
                pos = backward
                try_pos = 0

                continue
            else: #바다면
                end_flag = True
                break
    if end_flag:#더 이상 이동 불가능
        break
    else: # 갈 수 있으면
        #print(pos, d, pos_to_go, map_to_go)
        try_pos = 0 #초기화
        pos = pos_to_go #이동
        map[pos_to_go[0]][pos_to_go[1]] = 2 #갔음 체크
        result += 1 #이동횟수 증가

print(result)
''' #게임 구현
#기출
'''
score = input()
l = len(score)
if sum([int(i) for i in score[:l//2]]) == sum([int(i) for i in score[l//2:]]):
    print("LUCKY")
else:
    print("READY")
''' #럭키스트레이트
'''
from collections import defaultdict
s_input = input()
dict = defaultdict(int)
sum = 0
result = ""
for s in s_input:
    if s.isdigit():
        sum += int(s)
    else:
        dict[s] += 1
for s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if s in dict.keys():
        result += s*dict[s]
result += str(sum)
print(result)
'''