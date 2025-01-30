n = int(input())

ans = 0

for i in range(1, int(n**(1/2))+1):
    if not n%i:
        if i*i == n:
            ans += 1
            continue
        ans += 2

print(ans)