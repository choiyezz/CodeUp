# 변수는 자료형을 가진 어떤값을 저장할 수 있는 기억공간
# input() 으로 입력받은 내용(오른쪽 값)을 변수명(왼쪽) 에 대입한다. ( = : 대입연산자 )

# 파이썬은 변수 선언시 자료형을 사용하지 않기때문에 input 을 사용할때는 문자, 정수, 실수 구분이 필요하다.

# 문자 입력
c = input()
print(c)

# 정수 입력
n = int(input())
print(n)

# 실수 입력
f = float(input())
print(f)

# 정수 2개 입력받기
a, b = map(int, input().split())
print(a)
print(b)

# 문자 2개 입력받기
c, d = input().split()
print(c)
print(d)

# 실수 1개를 입력받아 줄을 바꿔 3번 출력
f = float(input())
print(f)
print(f)
print(f)