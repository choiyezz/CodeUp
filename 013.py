"""
while 조건식:

for i in range(끝): -- (끝 - 1) 까지만 포함
for i in range(시작, 끝):
for i in range(시작, 끝, 증감):
"""

# 0이 입력되면 종료
while True:
    a = int(input())
    if a != 0:
        print(a)
    else:
        break

# 카운트다운1
a = int(input())
while a != 0:
    print(a)
    a -= 1

# 카운트다운2
a = int(input())
while a > 0:
    a -= 1
    print(a)

# 알파벳 출력
a = ord(input())
b = ord('a')
while b <= a:
    print(chr(b), end=' ')
    b += 1

# 입력받은 수까지 출력1
a = int(input())
i = 0
while i <= a:
    print(i)
    i += 1

# 입력받은 수까지 출력2
a = int(input())
for i in range(a+1):
    print(i)



