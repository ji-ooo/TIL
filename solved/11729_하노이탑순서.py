N = int(input())
dp = [[] for _ in range(N+1)]
dp[1].append([1, 3])
for i in range(2, N+1):
    for x in dp[i-1]:
        tmp = x[:]
        if (x[0] == 2 and x[1] == 3) or (x[0] == 3 and x[1] == 2):
            tmp = x[::-1]
        else:
            if x[0] == 2 or x[0] == 3:
                tmp[0] = 5 - tmp[0]
            if (x[1] == 2) or (x[1] == 3):
                tmp[1] = 5 - tmp[1]
        dp[i].append(tmp)

    dp[i].append([1, 3])

    for x in dp[i-1]:
        tmp = x[:]
        if (x[0] == 1 and x[1] == 2) or (x[0] == 2 and x[1] == 1):
            tmp = x[::-1]
        else:
            if x[0] == 1 or x[0] == 2:
                tmp[0] = 3 - tmp[0]
            if x[1] == 1 or x[1] == 2:
                tmp[1] = 3 - tmp[1]
        dp[i].append(tmp)
print(len(dp[N]))
for i in dp[N]:
    print(*i)
