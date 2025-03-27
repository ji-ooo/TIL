N, M = map(int, input().split())

K, *kp = map(int, input().split())

kn = [0 for _ in range(N+1)]
que = []
for i in kp:
    kn[i] = 1
    que.append(i)

link = {i:set() for i in range(1, N+1)}
party = []
for _ in range(M):
    P, *p = map(int, input().split())
    party.append(p)

    for x in range(P):
        for y in range(P-x):
            link[p[x]].add(p[y])
            link[p[y]].add(p[x])

while que:
    x = que.pop()
    for nxt in link[x]:
        if kn[nxt]:
            continue

        kn[nxt] = 1
        que.append(nxt)

ans = 0
for pt in party:
    for pn in pt:
        if kn[pn]:
            break
    else:
        ans += 1

print(ans)
