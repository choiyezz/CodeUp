"""
출석번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력
"""
# 이상한 출석번호 부르기2
n = int(input())
rlist = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    print(rlist[i], end=' ')

