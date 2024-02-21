import sys
sys.stdin = open('5177.txt')


def heap_sort(v):
    par = v//2
    if par < 0:
        return
    else:
        if tree[par] > tree[v]:
            tree[v], tree[par] = tree[par], tree[v]
            heap_sort(par)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]
    node_num = 1
    for num in map(int, input().split()):
        tree.append(num)
        heap_sort(node_num)
        node_num += 1

    result = 0
    while N:
        N //= 2
        result += tree[N]

    print(f'#{tc} {result}')


