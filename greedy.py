'''
import random

#random.seed(2)
#n = 5
n = int(input())
#fear = [random.randint(1, n) for i in range(n)]
fear = list(map(int, input().split()))

g_num = 0

fear.sort()
fear = fear[::-1]


group = []
while fear:
    if not group: #그룹이 비어있으면
        group.append(fear.pop())
    if max(group) > len(group):  # 최대 공포수가 그룹 인원수보다 클 때
        group.append(fear.pop())
    else: #최대 공포수가 그룹 인원수보다 작거나 같다면
        g_num += 1 #그룹수 증가
        group = [] #그룹 초기화

print(g_num)
''' #모험가 길드
'''
line = list(map(int, list(input())))
print(line)

result = 0
if len(line) == 1:
    result = line[0]
else:
    result = line[0]
    for i in range(len(line)-1):
        if result + line[i+1] >= result * line[i+1]:
            result = result + line[i+1]
        else:
            result = result * line[i+1]

print(result)
''' #곱하기 혹은 더하기
'''#실패
line = [int(i) for i in list(input())]

index_list = []
gini = 1.0 - line.count(0)/len(line) * line.count(1)/len(line)
result = 0
while gini != 1.0:
    index = [0,0]
    for i in range(len(line)-1):
        if line[i] == line[i + 1]:
            index[1] += 1
        else:
            index_list.append(index)
            index = [i+1,i+1]
    index_list.append(index)
    print(index_list)
    index = min(index_list, key=(lambda i: i[1]-i[0]))
    line[index[0]:index[1]+1] = [1-a for a in line[index[0]:index[1]+1]]

    gini = 1.0 - line.count(0)/len(line) * line.count(1)/len(line)

    index_list = []
    result += 1

print(result)
''' #문자열뒤집기 실패
'''
line = [int(i) for i in list(input())]
result = 0
count0 = 0 #0으로 바뀌는 횟수
count1 = 0 #1로 바뀌는 횟수

if line[0]: #시작이 1이면
    count0 += 1 #0으로 바뀜
else:
    count1 += 1

for i in range(len(line)-1):
    if line[i] != line[i+1]: #다르면
        if line[i+1]: #0->1
            count0 += 1
        else: #1->0
            count1 += 1
    #print(count0, count1)
result = min(count1, count0)

print(result)
''' #문자열뒤집기
'''
n = int(input())
data = list(map(int, input().split()))
data.sort()
data = data[::-1]
result = 1
while True:
    if result in data:
        result += 1
        continue
    else:
        tmp = result
        for i in range(len(data)):
            tmp -= data[i]
            #print(tmp)
            if tmp == 0:
                break
            elif tmp < 0:
                tmp += data[i]
        #print(result, tmp)
        if tmp != 0:
            break
    result += 1

print(result)
#''' #만들 수 없는 금액
'''
n, m = [int(i) for i in input().split()]
weights = [int(i) for i in input().split()]
weights.sort()

result = 0
for i in range(n-1):
    result += [weights[i] != w for w in weights[i:]].count(True)

print(result)
''' #볼링공 고르기
