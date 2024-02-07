N = int(input())
boxes = [1001]
boxes.extend(list(map(int, input().split())))

dp = [1 for _ in range(N+1)]
for i in range(2, N+1):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    
print(max(dp))
print(dp)