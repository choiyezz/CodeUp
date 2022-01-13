# 언제까지 더해야 할까?2
a = int(input())
sum = 0
i = 1
while True:
    sum += i
    i += 1
    if sum >= a:
        break
print(sum)
