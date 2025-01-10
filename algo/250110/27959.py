N, M = map(int, input().split())

bal = 100 * N

if M <= bal:
    print('Yes')
else:
    print('No')