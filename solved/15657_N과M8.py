N, M = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

def per(n, l):
    if len(l) == M:
        print(*l)
        return
    else:
        for i in range(N):
            if i >= n:
                l.append(num[i])
                per(i, l)
                l.pop()

per(0, [])