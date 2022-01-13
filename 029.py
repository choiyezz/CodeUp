"""
출석번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력

"""
# 이상한 출석번호 부르기
num = int(input())
rlist = map(int, input().split())
nlist = []

for i in range(24):
    nlist.append(0)

for i in rlist:
    nlist[i] += 1

for i in range(1, 24):
    print( nlist[i], end=' ')





