N = int(input())
M = int(input())
c = list(map(int, input().split()))

cand = dict()

for i in c:
    if i in cand:
        cand[i] += 1
        continue

    if len(cand) == N:
        tmp = M
        for k in reversed(cand.keys()):
            if tmp >= cand[k]:
                tmp = cand[k]
                mkey = k

        cand.pop(mkey)

    cand[i] = 1

ans = sorted(cand.keys())

print(*ans)