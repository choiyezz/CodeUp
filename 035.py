"""
개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.
성실한 개미가 이동한 경로를 9로 표시해 출력한다.
"""
# 성실한 개미
mylist = [list(map(int, input().split())) for _ in range(10)]

x, y = 2, 2
x -= 1
y -= 1
while True:
    if mylist[x][y] == 2:
        mylist[x][y] = 9
        break

    mylist[x][y] = 9
    if mylist[x][y+1] != 1:
        y += 1
    elif mylist[x+1][y] != 1:
        x += 1
    elif (mylist[x][y+1] == 1 and mylist[x+1][y] == 1) or x == 8 and y == 8:
        break

for i in range(10):
    for j in range(10):
        print(mylist[i][j], end=' ')
    print()
