def sol(k):
    global cnt 

    if k == n:
        cnt += 1
        return
    
    for i in range(n):
        if not visited[i] and not diag[k + i] and not diag_rev[n - 1 + k - i]:
            visited[i] = diag[k + i] = diag_rev[n - 1 + k - i] = 1
            sol(k + 1)
            visited[i] = diag[k + i] = diag_rev[n - 1 + k - i] = 0


n = int(input())
arr = [[0] * n for _ in range(n)]
visited = [0] * n
diag = [0] * (2 * n - 1)
diag_rev = [0] * (2 * n - 1)

cnt = 0
sol(0)
print(cnt)
