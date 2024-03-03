T = int(input())

prime = []
for i in range(2, 10001):
    for x in range(2, 1001):
        if i != x and i%x == 0:
            break
    else:
        prime.append(i)
    

for _ in range(T):
    N = int(input())
    n = N//2 + N%2
    if N%2 == 0 and n in prime:
        result = [n, n]
    else:
        tmp = 10000
        result = [n, n]
        for i in range(len(prime)):
            for j in range(i, len(prime)):
                if prime[i] + prime[j] == N:
                    if tmp > prime[j] - prime[i]:
                        tmp = prime[j] - prime[i]
                        result = [prime[i], prime[j]]
                    break
            if i >= n:
                break
    print(*result)