import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip())))

mx_sq = min(N, M)-1
ans = 0
while mx_sq > 0:
    for i in range(N):
        for j in range(M):
            d = mx_sq
            nx, ny = i+d, j+d

            if nx < N and ny < M:
                if arr[i][j] == arr[i][ny] == arr[nx][j] == arr[nx][ny]:
                    ans = d
            
        if ans:
            break
    if ans:
        break

    mx_sq -= 1
ans += 1
ans **= 2
print(ans)
            