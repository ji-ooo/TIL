import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort()
ans = 0

prev = -L - 1
for s, e in arr:
    if prev < s:
        prev = s
    
    if prev < e:
        tmp = (e - prev) // L + (1 if (e - prev) % L else 0)
        ans += tmp
        prev += L * tmp

print(ans)
