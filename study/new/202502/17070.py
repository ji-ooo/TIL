import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for i in range(N):
    for j in range(N):
        if not i and not j:
            continue

        if arr[i][j]:
            continue

        if j:
            dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
        
        if i:
            dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
        
        if i and j:
            if not arr[i-1][j] and not arr[i][j-1]:
                dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[-1][-1]))