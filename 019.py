# 369게임1
a = int(input())
for i in range(1, a+1):
    if (i % 10 == 3) or (i % 10 == 6) or (i % 10 == 9):
        if (i // 10 == 3) or (i // 10 == 6) or (i // 10 == 9):
            print('XX', end=' ')
        else:
            print('X', end=' ')
    elif (i // 10 == 3) or (i // 10 == 6) or (i // 10 == 9):
        print('X', end=' ')
    else:
        print(i, end=' ')


# 369게임2
a = int(input())
for i in range(1, a+1):
    count = 0
    ten = i // 10
    one = i % 10

    if (ten != 0) and (ten % 3 == 0):
        count += 1
    if (one != 0) and (one % 3 == 0):
        count += 1

    if count == 1:
        print('X', end=' ')
    elif count == 2:
        print('XX', end=' ')
    else:
        print(i, end=' ')
