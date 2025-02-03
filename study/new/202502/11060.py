N = int(input())

maze = list(map(int, input().split()))

dp = [1e9 for _ in range(N)]
dp[0] = 0

for i in range(N):
    dist = maze[i]
    for j in range(1, dist+1):
        if i + j < N:
            dp[i + j] = min(dp[i + j], dp[i] + 1)

print(dp[-1] if dp[-1] != 1e9 else -1)