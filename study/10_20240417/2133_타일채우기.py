N = int(input())
if N%2 == 1:
    print(0)
else:
    n = N//2
    dp = [0] * 16
    dp[1] = 3
    dp[2] = 11
    for i in range(3, n+1):
        dp[i] = dp[i-1] * 3 + sum(dp[:i-1])*2 + 2

    print(dp[n])

'''
N이 홀수면 경우의수 없음

N = 2
3

N = 4
11

N = 6





'''