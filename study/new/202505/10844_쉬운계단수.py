n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]
e = int(1e9)

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] % e
        elif j == 9:
            dp[i][j] = dp[i-1][8] % e
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % e

ans = sum(dp[n]) % e
print(ans)
