N = int(input())
arr = list(map(int, input().split()))

M = 0
m = 1e9

for i in range(N):
    if arr[i] > M:
        M = arr[i]
    if arr[i] < m:
        m = arr[i]

lastM = -1
lastm = -1

ans = N+1

for i in range(N):
    if arr[i] == M:
        lastM = i
        if lastm != -1:
            ans = min(ans, i - lastm + 1)
    
    if arr[i] == m:
        lastm = i
        if lastM != -1:
            ans = min(ans, i - lastM + 1)

print(ans)