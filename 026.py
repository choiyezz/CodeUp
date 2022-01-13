# 등비수열
start, r, n = map(int, input().split())
for i in range(1, n):
    start *= r
print(start)
