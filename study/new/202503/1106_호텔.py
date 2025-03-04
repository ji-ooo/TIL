import sys
input = sys.stdin.readline

C, N = map(int, input().split())
# C명 채우기
costs = [list(map(int, input().split())) for _ in range(N)]
# c원 당 n명
# costs.sort(key= lambda x : - x[1] / x[0])

dp = [1e9 for _ in range(C + 100)]
dp[0] = 0

for c, n in costs:
    for i in range(n, len(dp)):
        dp[i] = min(dp[i - n] + c, dp[i])

print(min(dp[C:]))
print(dp)