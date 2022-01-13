# 수열
start, mul, d, n = map(int, input().split())
for i in range(1, n):
    start = start * mul + d
print(start)
