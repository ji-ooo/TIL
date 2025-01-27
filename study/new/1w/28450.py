N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

H = int(input())

dp = [[0]*(M) for _ in range(N)]

dp[0][0] = arr[0][0]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + arr[i][0]
    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + arr[0][j]

        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]

if dp[-1][-1] > H:
    print("NO")
else:
    print("YES")
    print(dp[-1][-1])