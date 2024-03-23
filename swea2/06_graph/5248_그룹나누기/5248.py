import sys
sys.stdin = open('5248.txt')


def make_set(N):
    return [i for i in range(N+1)]


def find_set(x):
    if parents[x] == x:
        return x

    return find_set(parents[x])


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    parents = make_set(N)
    line = list(map(int, input().split()))

    for i in range(M):
        a, b = line[2*i], line[2*i+1]
        union(a, b)

    groups = set(find_set(i) for i in range(1, N+1))

    print(f'#{tc} {len(groups)}')
