
# 시간 입력받아 그대로 출력하기
# : 기준으로 자르기
a, b = input().split(":")
# : 를 사이에 두고 출력
print(a, b, sep=":")

# 연도.월.일 을 입력받아 일-월-연도 순서로 출력
a, b, c = input().split(".")
print(c, b, a, sep="-")

# 주민번호 입력받아 모두 붙여 출력
a, b = input().split("-")
print(a+b)


# 단어 1개 입력받아 나누어 출력
s = input()
print(s[0])
print(s[1])

# 6자리 연월일(YYMMDD) 입력받아 나누어 출력
s = input()
print(s[0:2], end=' ')
print(s[2:4], end=' ')
print(s[4:6])

# 시:분:초 입력받아 분만 출력하기
s = input().split(":")
print(s[1])