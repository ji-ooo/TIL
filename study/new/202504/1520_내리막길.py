import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    if x == N - 1 and y == M - 1:
        return 1
    
    cnt = 0
    now = arr[x][y]

    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if now > arr[nx][ny]:
                cnt += dfs(nx, ny)
    
    dp[x][y] = cnt

    return cnt

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

dp = [[-1 for _ in range(M)] for _ in range(N)]

print(dfs(0, 0))