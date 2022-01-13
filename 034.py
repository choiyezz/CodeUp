"""
첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d: 가로는 0, 세로는 1), 좌표(x, y)가 입력된다.
좌표는 가장 왼쪽의 위치 또는 가장 위쪽의 위치이다.
---
모든 막대를 놓은 격자판의 상태를 출력한다.
막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
"""
# 설탕과자 뽑기
height, width = map(int, input().split())
mylist = [[0 for i in range(width)] for j in range(height)]

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())

    for j in range(l):
        mylist[x-1][y-1] = 1
        if d == 0:
            y += 1
        else:
            x += 1

for i in range(height):
    for j in range(width):
        print(mylist[i][j], end=' ')
    print()
