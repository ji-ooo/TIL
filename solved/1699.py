import sys
input = sys.stdin.readline

N = int(input())

dp = [i for i in range(N+1)]
dp[0] = 0

for i in range(1, N+1):
    for j in range(1, int(i**(1/2)+1)):
        dp[i] = min(dp[i], dp[i-j**2]+1)

print(dp[N])
