import sys
sys.stdin = open('5178.txt')


def node_sum(node):
    left = node*2
    right = node*2 + 1
    if right <= N:
        tree[node] = tree[left] + tree[right]
    elif left <= N:
        tree[node] = tree[left]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        v, n = map(int, input().split())
        tree[v] = n

    for i in range(N-1, 0, -1):
        if tree[i] == 0:
            node_sum(i)

    print(f'#{tc} {tree[L]}')