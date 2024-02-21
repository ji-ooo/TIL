import sys
sys.stdin = open('5174.txt')


def cnt_subtree(tree1, tree2, start):
    global cnt
    if tree1[start] != -1:
        cnt += 1
        cnt_subtree(tree1, tree2, tree1[start])

    if tree2[start] != -1:
        cnt += 1
        cnt_subtree(tree1, tree2, tree2[start])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree1 = [-1 for _ in range(E+2)]
    tree2 = [-1 for _ in range(E+2)]

    line = list(map(int, input().split()))

    for _ in range(E):
        e, s = line.pop(), line.pop()

        if tree1[s] == -1:
            tree1[s] = e
        else:
            tree2[s] = e

    start = N
    cnt = 1
    cnt_subtree(tree1, tree2, start)

    print(f'#{tc} {cnt}')
