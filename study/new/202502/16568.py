import sys
input = sys.stdin.readline

N, a, b = map(int, input().split())

dp = [1e9] * (N+1)
dp[0] = 0

move = [0, a, b]

for i in range(N):
    for m in move:
        if i + m + 1 > N:
            continue

        dp[i + m + 1] = min(dp[i + m + 1], dp[i] + 1)

print(dp[-1])

