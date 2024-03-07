N = int(input())
M = int(input())

k = M-N

n = 1
for i in range(1, N+k):
    n *= i

r = 1
for i in range(1, N):
    r *= i

l = 1
for i in range(1, k+1):
    l *= i

print(n //(r*l))