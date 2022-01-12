"""
if 조건식:
elif 조건식:
else:
"""
# 짝수 출력
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 짝/홀 출력
a, b, c = map(int, input().split())
if a % 2 == 0:
    print("even")
else:
    print("odd")
if b % 2 == 0:
    print("even")
else:
    print("odd")
if c % 2 == 0:
    print("even")
else:
    print("odd")

# 분류하기( 정수를 음/양, 짝/홀 구분)
a = int(input())
if a < 0:
    if a % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if a % 2 == 0:
        print('C')
    else:
        print('D')

# 점수 평가
a = int(input())
if a >= 90:
    print('A')
elif a >= 70:
    print('B')
elif a >= 40:
    print('C')
else:
    print('D')

# 평가를 다르게 출력하기
a = input()
if a == 'A':
    print("best!!!")
elif a == 'B':
    print("good!!")
elif a == 'C':
    print("run!")
elif a == 'D':
    print("slowly~")
else:
    print("what?")

# 계절 출력
a = int(input())
if a == 12 or a < 3:
    print("winter")
elif a < 6:
    print("spring")
elif a < 9:
    print("summer")
elif a < 12:
    print("fall")
