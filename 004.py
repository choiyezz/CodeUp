"""
16진수, hexadecimal
    -- %x(소문자), %X(대문자)
    -- 0 1 2 3 4 5 6 7 8 9 a b c d e f

8진수, octal
    -- %o
    -- 0 1 2 3 4 5 6 7 10 11 12 ...
"""

# 10진수를 입력받아 16진수로 출력하기
a = int(input())
print('%x' % a)

a = int(input())
print('%X' % a)

# 16진 정수 입력받아 8진수로 출력하기
a = int(input(), 16)
print('%o' % a)

# 영문자 입력받아 10진수로 출력
# ord() : 어떤 문자의 순서 위치(ordinal position), 입력받은 문자를 10진수 유니코드 값으로 변환
a = ord(input())
print(a)

# 정수 입력받아 유니코드 문자로 변환
# chr() : 정수값 -> 문자 / ord() : 문자 -> 정수값
a = int(input())
print(chr(a))




