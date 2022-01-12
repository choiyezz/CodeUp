"""
논리연산
boolean : True / False(0, "", '')

Not 연산
not True == False
not False == True

AND 연산 : 모두 True 이면 True
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1

OR 연산 : 하나라도 True 이면 True
A B A|B
0 0 0
0 1 1
1 0 1
1 1 1

XOR 연산 : True, False 가 서로 다르면 True
( A & not B ) | ( not A & B )
A B (A xor B)
0 0 0
0 1 1
1 0 1
1 1 0
"""

# 정수의 참 거짓 ( 0 이외의 정수는 모두 True )
a = int(input())
print(bool(a))

# 참 거짓 바꾸기
a = bool(int(input()))
print(not a)

# 둘 다 참일 경우만 참 출력
a, b = map(int, input().split())
print(bool(a) and bool(b))

# 하나라도 참이면 참 출력
print(bool(a) | bool(b))

# 참, 거짓이 서로 다를때 참 출력
a, b = map(int, input().split())
c, d = bool(a), bool(b)
print((c and (not d)) or ((not c) and d))

# 참, 거짓이 서로 같을때 참 출력
print((c and d) or (not c and not d))

# 둘 다 거짓일때 참 출력
print(not(a or b))


