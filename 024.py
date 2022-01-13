# 3의 배수는 통과
a = int(input())
for i in range(1, a+1):
    if i % 3 == 0:
        continue
    print(i, end=' ')