N = int(input())
boxes = [0]
boxes.extend(list(map(int, input().split())))

dp = [1 for _ in range(N+1)]
print(boxes, dp)
for i in range(2, N+1):
    k = 1
    if boxes[i] == max(boxes[:i+1]):
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]
    
print(max(dp))

'''
boxes[i]보다 작은 box 중 가장 dp가 큰 box의 인덱스 뽑기 ?
'''