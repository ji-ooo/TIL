N = int(input())

n = N
cnt = 0
while True:
    cnt += 1
    if n < 10:
        a = 0
    else:
        a = n//10
    b = n%10

    n = a + b
    c = n%10
    n = b*10 + c

    if n == N:
        break

print(cnt)