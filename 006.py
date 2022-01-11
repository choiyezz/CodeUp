# 정수 2개로 거듭제곱 계산
a, b = map(int, input().split())
print(a**b)

# 실수 2개로 거듭제곱 계산
a, b = map(float, input().split())
print(a**b)

# 정수 2개로 나눈 몫 계산
a, b = map(int, input().split())
print(a // b)   # 3
print(a / b)    # 3.3333333333333335

# 정수 2개로 나눈 나머지 계산
a, b = map(int, input().split())
print(a % b)    # 1

# 실수의 소숫점이하 자리 변환
a = float(input())
"""
format( 값, "..." ) , ".2f" : 소숫점 3번째 자리에서 반올림하여 2번째 짜리까지 나타냄
컴퓨터에서 실수는 정확한 값이 아니라 컴퓨터가 최대로 표현 가능한 근사값이므로 유효숫자는 중요하다.
"""
print(format(a, ".2f"))

# 실수 2개로 나눈 결과 계산, 소숫점 넷째자리에서 반올림한다
a, b = map(float, input().split())
print(format(a / b, ".3f"))

# 정수 2개 입력받아 자동계산
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a / b, ".2f"))

# 정수 3개로 합과 평균 계산
a, b, c = map(int, input().split())
sum = a + b + c
print(sum, format(sum / 3, ".2f"))

