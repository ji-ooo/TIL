N = int(input())
n = str(N)

length = len(n)
ans = 0
cnt = 1
while cnt < length:
    ans += 9 * 10 ** (cnt-1) * cnt
    N -= 9 * 10 ** (cnt-1)
    cnt += 1
ans += N*cnt
print(ans)