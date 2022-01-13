# 등차수열
start, step, n = map(int, input().split())
for i in range(2, n+1):
    start += step
print(start)



