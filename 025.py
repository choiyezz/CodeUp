# 등차수열
start, d, n = map(int, input().split())
for i in range(1, n):
    start += d
print(start)
