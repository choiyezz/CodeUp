"""
비트 단위 논리 연산
~(not), &(and), |(or), ^(xor), <<, >>

1 : 0000 0000 0000 0001
~1 : 1111 1111 1111 1110
~n : -n - 1

2의 보수 : 음의 정수를 표현
-1 : ~1 ( 1111 1111 1111 1110 ) + 1 = 1111 1111 1111 1111
-n : ~n + 1
"""


# 비트단위로 NOT 하여 출력
a = int(input())
print(~a)

# 비트단위로 AND 하여 출력
a, b = map(int, input().split())
print(a & b)

# 비트단위로 OR 하여 출력
print(a | b)

# 비트단위로 XOR 하여 출력
print(a ^ b)
