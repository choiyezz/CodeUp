# 등차수열
start, d, n = map(int, input().split())
for i in range(2, n+1):
    start += d
print(start)



