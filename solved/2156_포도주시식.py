N = int(input())

w = [0] + [int(input()) for _ in range(N)]

dp = [0 for _ in range(N+1)]
dp[1] = w[1]


for i in range(2, N+1):
    dp[i] = max(dp[i-1], w[i] + w[i-1] + dp[i-3], w[i] + dp[i-2])
print(dp[-1])