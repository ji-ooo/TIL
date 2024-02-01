from math import trunc

X, Y = map(int, input().split())

z = Y/X*100
Z = trunc(z)

v = X//100
cnt = 0
i = 2
while trunc(z) != Z+1:
    v = X//10**i
    while z-(Z+1) < 0:
        X += v
        Y += v
        cnt += v
        z = Y/X*100

    while z-(Z+1) > 0:
        X -= v
        Y -= v
        cnt -= v
        z = Y/X*100
    print(z)
    i += 1
print(z, Z, cnt)


'''
X += a
Y += a
trunc(z) 가 +1 될때까지

'''
