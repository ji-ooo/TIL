N = int(input())
link = list(map(int, input().split()))
m = int(input())

def dfs(v):
    link[v] = -2

    for i in range(N):
        if v == link[i]:
            dfs(i)

dfs(m)

ans = 0

for i in range(N):
    p = link[i]
    if p != -2:
        if i in link:
            continue

        ans += 1

print(ans)