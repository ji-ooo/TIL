import sys
input = sys.stdin.readline


def dfs(idx):
    que = [idx]
    visit = [0] * (N+1)
    visit[idx] = 1
    cnt = 1

    while que:
        v = que.pop()
        for c in com[v]:
            if not visit[c]:
                visit[c] = 1
                cnt += 1
                que.append(c)
    
    return cnt


N, M = map(int, input().split())
com = {i: [] for i in range(1, N+1)}

for _ in range(M):
    c, p = map(int, input().split())
    com[p].append(c)

ans = []
maxi = 0

for i in range(1, N+1):
    tmp = dfs(i)
    if maxi > tmp:
        continue
    
    if maxi < tmp:
        maxi = tmp
        ans = [i]
    else:
        ans.append(i)

print(*ans)