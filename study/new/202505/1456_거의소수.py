A, B = map(int, input().split())

bnd = int(B ** 0.5)

prime = [1] * (bnd + 1)
prime[1] = False

for i in range(2, bnd + 1):
    if prime[i]:
        if i**2 > bnd:
            break

        for j in range(i**2, bnd + 1, i):
            prime[j] = False
        
cnt = 0

for i in range(1, len(prime)):
    if prime[i]:
        tmp = i**2

        while True:
            if tmp < A:
                tmp *= i
                continue

            if tmp > B:
                break

            tmp *= i
            cnt += 1

print(cnt)