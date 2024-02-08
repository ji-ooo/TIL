import sys
sys.stdin = open('5102.txt')

from collections import deque


def bfs(que, visited):
    global dist
    global result
    dist += 1
    nxt_lst = deque([])
    while que:
        v = que.pop()
        visited.append(v)
        nxt = link[v]
        for i in nxt:
            if i not in visited:
                nxt_lst.append(i)
                if i == G:
                    result = dist
                    return
    if nxt_lst:
        bfs(nxt_lst, visited)
    else:
        return


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    link = {i:[] for i in range(1, V+1)}
    for _ in range(E):
        a, b = map(int, input().split())
        link[a].append(b)
        link[b].append(a)
    S, G = map(int, input().split())

    visited = []
    que = deque([S])
    dist = 0
    result = 0
    bfs(que, visited)

    print(f'#{tc} {result}')
