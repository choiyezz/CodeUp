"""
같은날 동시에 가입한 3명의 사람들이 문제를 푸는 날짜가 매우 규칙적일 때,
다 같이 문제를 풀게 되는 날은 언제일까?
"""
# 함께 문제 푸는 날
a, b, c = map(int, input().split())
d = 1
while True:
    if (d % a == 0) and (d % b == 0) and (d % c == 0):
        break
    d += 1
print(d)
