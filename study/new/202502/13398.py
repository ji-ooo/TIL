import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 없애지 않고 그냥 더한 합의 최대가 dp[0]에 갱신
# 없애고 쭉 더해오고 있는 합의 최대가 dp[1]에 갱신
dp = [[0] * n for _ in range(2)]
dp[0][0] = arr[0]
ans = arr[0]

for i in range(1, n):
    # 없애지 않은 합이랑 지금 수를 비교
    dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
    # 없애고 더해 온 합이랑, 지금 수를 없앴다 가정하고 없애지 않은 합이랑 비교
    dp[1][i] = max(dp[1][i-1] + arr[i], dp[0][i-1])
    # 최대를 항상 저장 해줘야 함
    ans = max(ans, dp[0][i], dp[1][i])

print(ans)