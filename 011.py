"""
3항연산
x if( ... ) else y
if가 True 이면 x, False 이면 y
"""

# 큰 값 출력
a, b = map(int, input().split())
c = (a if(a >= b) else b)
print(c)

# 가장 작은 값 출력
a, b, c = map(int, input().split())
d = ((a if(a < b) else b) if((a if(a > b) else b) < c) else c)
print(d)
