import sys
sys.stdin = open('1232.txt')


def cal(node, v):
    c = node[0]
    now = v
    if node[1]:
        left, right = map(int, node[1])

    if type(c) is int:
        return c
    else:
        num_l = cal(tree[left], left)
        num_r = cal(tree[right], right)

    if c == '+':
        tree[now] = num_l + num_r
    elif c == '-':
        tree[now] = num_l - num_r
    elif c == '*':
        tree[now] = num_l * num_r
    elif c == '/':
        tree[now] = num_l // num_r
    return tree[now]


for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        n, c, *etc = map(str, input().split())
        if c.isdigit():
            c = int(c)
        tree[i] = [c, etc]

    v = 1
    cal(tree[v], v)
    print(f'#{tc} {tree[1]}')
