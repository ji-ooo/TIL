import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import deque


def dfs(i, cnt):
    visited[i] = 1
    for to in edge[i]:
        if A[to-1] == '1':
            cnt += 1
        elif not visited[to] and A[to-1] == '0':
            cnt = dfs(to, cnt)

    return cnt


N = int(input())

A = str(input())

edge = {i:[] for i in range(N+1)}
result = 0
for _ in range(N-1):
    u, v = map(int, input().split())

    edge[u].append(v)
    edge[v].append(u)

    if A[u-1] == A[v-1] == '1':
        result += 2

# print(edge)
visited = [0] * (N+1)
for i in range(1, N+1):
    s = A[i-1]
    if s == '0' and not visited[i]:
        tmp = dfs(i, 0)
        result += tmp * (tmp-1)

print(result)
'''
실내 1 실외 0
1에서 시작, 끝
중간에 1 안됨
10....01
경로 개수 출력

완탐 해봐야됨 결국
모든 1에서 시작 하고,
그냥 다 가보면서
1 만나면 갯수 +1 하고 return
0 만나면 que에 넣고 방문처리 하는건데
방문처리 어케 함?

실외에서 탐색 시작해서
인접한 실내 갯수 * 실내 갯수 -1

'''