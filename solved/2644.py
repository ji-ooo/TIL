from collections import deque


def bfs(que, cnt):
    global visited
    
    nxt_lst = deque([])
    while que:
        v = que.pop()
        if v != x:
            visited[v] = cnt
        
        nxt = link[v]
        for i in nxt:
            if not visited[i]:
                nxt_lst.append(i)
    
    if nxt_lst:
        bfs(nxt_lst, cnt+1)
        

N = int(input())
x, y = map(int, input().split())
M = int(input())
link = {i:[] for i in range(N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

cnt = 0
que = deque([x])
visited = {i:False for i in range(N+1)}
visited[x] = 0

bfs(que, cnt)

if visited[y]:
    print(visited[y])
else:
    print(-1)
print(link)
print(visited)