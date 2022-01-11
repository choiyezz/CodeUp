# 정수를 입력받아 부호 변경
a = int(input())
print(-a)

# 문자를 입력받아 다음 문자 출력
# ord() 로 문자값을 정수값으로 바꿔 chr() 로 정수값을 문자로 출력
a = ord(input())
print(chr(a+1))


# 정수 2개 입력받아 차 계산
a, b = map(int, input().split())
print(a - b)

#실수 2개 입력받아 곱 계산
a, b = map(float, input().split())
print(a * b)

# 단어 여러번 출력 ( 문자 * 정수 )
w, n = input().split()
print(w * int(n))

# 문장 여러번 출력
n = int(input())
s = input()
print(s * int(n))

