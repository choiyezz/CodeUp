"""
1초 동안 마이크로 소리강약을 체크하는 횟수를 h
한 번 체크한 값을 저장할 때 사용하는 비트수를 b
좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c
(모노는 1개, 스테레오는 2개의 트랙)
녹음할 시간(초) s가 주어진다.

실제로, 일반적인 CD 음질(44.1KHz, 16bit, 스테레오)로 1초 동안 저장하려면
44100 * 16 * 2 * 1 bit의 저장공간이 필요한데,
44100*16*2*1/8/1024/1024 로 계산하면 약 0.168 MB 정도가 필요하다.
"""

# 소리파일 저장용량 계산하기
h, b, c, s = map(int, input().split())
save = (h * b * c * s)/8/1024/1024
print(format(save, ".1f"), "MB")