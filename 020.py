# 빛 섞어 색 만들기
# red, green, blue 를 섞어 만들 수 있는 모든 경우의 조합과 색의 가짓수
red, green, blue = map(int,input().split())
count = 0
for i in range(red):
    for j in range(green):
        for k in range(blue):
            print(i, j, k)
            count += 1
print(count)

