import sys
sys.stdin = open('input.txt')

N,K = int(input()),int(input())
# dp[i][j] : 1~i번째 색 중에서 j개의 색을 선택하는 경우의 수
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(K+1):
        if j==0:
            dp[i][j] = 1
            continue
        if j==1:
            dp[i][j] = i
            continue
        dp[i][j] += dp[i-1][j]
        dp[i][j] += dp[i-2][j-1] if i != N else dp[i-3][j-1]

        dp[i][j] %= 1000000003

print(dp[N][K])