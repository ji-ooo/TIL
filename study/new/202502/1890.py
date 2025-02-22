import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [(0, 1), (1, 0)]

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if not dp[x][y]:
            continue

        if x == N-1 and y == N-1:
            continue
            
        dist = arr[x][y]

        if x + dist < N:
            dp[x + dist][y] += dp[x][y]

        if y + dist < N:
            dp[x][y + dist] += dp[x][y]

print(dp[N-1][N-1])