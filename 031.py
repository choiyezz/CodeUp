"""
번호를 n번 무작위로 불렀을때, 가장 빠른 번호를 출력
"""
# 이상한 출석번호 부르기3
n = int(input())
rlist = list(map(int, input().split()))

minimum = rlist[0]
for i in range(len(rlist)):
    if minimum > rlist[i]:
        minimum = rlist[i]
print(minimum)