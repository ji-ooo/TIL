'''
S 신맛, 곱
B 쓴맛, 합
신맛과 쓴맛 차이가 가장 적게
'''
def cook(fd, S, B, start):
    global result

    if fd == N:
        if abs(S-B) < result:
            result = abs(S-B)
        return
    else:
        if fd == start:
            cook(fd + 1, S * s[fd], B + b[fd], start)
        else:
            cook(fd + 1, S * s[fd], B + b[fd], start)
            cook(fd + 1, S, B, start)

N = int(input())
s = []
b = []
for _ in range(N):
    sour, bitt = map(int, input().split())
    s.append(sour)
    b.append(bitt)


result = 1e9
for i in range(N):
    cook(i, 1, 0, i)
print(result)