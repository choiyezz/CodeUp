# 16진수 구구단
a = int(input(), 16)
for i in range(1, 16):
    # print('%X' % a, '*%X' % i, '=%X' % (a*i), sep='')
    print("%X*%X=%X" % (a, i, (a*i)))
