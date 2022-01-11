"""
쉬프트 연산
n = 8 인 경우 (1000)_2진수
n >> 1 : 4(010) 왼쪽에서 0(양의 정수)이나 1(음의 정수)이 1개 추가되며 나누기 2를 하는 형태로 동작한다.
            1개씩 밀리며 가장 오른쪽에 있는 1비트는 사라진다.
n << 1 : 16(10000) 오른쪽에서 0이 1개 추가되며 곱하기 2를 하는 형태로 동작한다.
"""

# 정수 입력받아 2배 곱하기
a = int(input())
print(a << 1)


# 2의 거듭제곱 배로 곱하기
a, b = map(int, input().split())
print(a << b)

