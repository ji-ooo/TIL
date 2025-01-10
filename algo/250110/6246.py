N, Q = map(int, input().split())

bal = [True] + [False] * N

for _ in range(Q):
    L, I = map(int, input().split())

    while L <= N:
        bal[L] = True
        L += I

print(bal.count(False))
