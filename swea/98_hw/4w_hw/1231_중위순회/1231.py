import sys
sys.stdin = open('1231.txt')


def inorder(tree, start):
    global ans
    left = start*2
    right = start*2 +1
    if left < len(tree):
        inorder(tree, left)

    ans += tree[start]

    if right < len(tree):
        inorder(tree, right)

    return ans


for tc in range(1, 11):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    for _ in range(N):
        v = list(map(str, input().split()))
        node = int(v[0])
        word = v[1]
        tree[node] = word
    ans = ''
    start = 1
    result = inorder(tree, start)

    print(f'#{tc} {result}')