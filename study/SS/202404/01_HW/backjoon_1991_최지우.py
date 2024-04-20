N = int(input())

tree = [list(map(str, input().split())) for _ in range(N)]


def preorder(i):
    cur, left, right = tree[i]

    print(cur, end='')

    if left != '.':
        for x in range(N):
            if left == tree[x][0]:
                preorder(x)

    if right != '.':
        for x in range(N):
            if right == tree[x][0]:
                preorder(x)


def inorder(i):
    cur, left, right = tree[i]

    if left != '.':
        for x in range(N):
            if left == tree[x][0]:
                inorder(x)

    print(cur, end='')

    if right != '.':
        for x in range(N):
            if right == tree[x][0]:
                inorder(x)


def postorder(i):
    cur, left, right = tree[i]

    if left != '.':
        for x in range(N):
            if left == tree[x][0]:
                postorder(x)

    if right != '.':
        for x in range(N):
            if right == tree[x][0]:
                postorder(x)

    print(cur, end='')


preorder(0)
print()
inorder(0)
print()
postorder(0)