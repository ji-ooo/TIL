import sys
sys.stdin = open('1238.txt')
from collections import deque

for tc in range(1, 11):
    N, start = map(int, input().split())

    link = {i: [] for i in range(1, 101)}
    line = list(map(int, input().split()))
    for i in range(N//2):
        s, e = line[2*i], line[2*i+1]
        link[s].append(e)

    que = deque([(start, 1)])
    visited = [0] * 101
    visited[start] = 1
    mx_cnt = 0

    while que:
        v = que.popleft()
        num, cnt = v
        mx_cnt = max(cnt, mx_cnt)
        cnt += 1
        for w in link[num]:
            if not visited[w]:
                visited[w] = cnt
                que.append((w, cnt))

    result = 0
    for i in range(100, 0, -1):
        if visited[i] == mx_cnt:
            result = i
            break
    print(f'#{tc} {result}')
