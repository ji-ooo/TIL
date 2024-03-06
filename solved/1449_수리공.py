N, L = map(int, input().split())
point = list(map(int, input().split()))
point.sort()

pipe = [0] * 1001

cnt = 0

for p in point:
    if not pipe[p]:
        for i in range(L):
            if p + i < 1001:
                pipe[p+i] = 1
        cnt += 1

print(cnt)
