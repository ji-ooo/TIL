import sys
from heapq import heappop, heappush
input = sys.stdin.readline

TC = int(input())

# 웜홀을 타면 시간이 반대로 감
# 한 지점에서 출발, 출발지까지 시간을 줄이면서 돌아올 수 있는지 여부

'''
웜홀을 반드시 한번은 타야함
웜홀을 탈 때 얻는 시간 이득이랑, 웜홀의 도착 -> 출발 까지 걸리는 최단거리랑 비교해보면 되는거 아닌가
조금이라도 이득이 생기면 계속 반복해서 감소시킬 수 있음

모든 웜홀에 대해서
웜홀 끝점 ~ 시작점 까지 도로만 타는 최단시간을 다 찾기
'''

for tc in range(TC):
    N, M, W = map(int, input().split())
    # 지점의 수, 도로의 개수, 웜홀의 개수
    # 도로는 방향 x, 웜홀은 방향 o
    road = {i:[] for i in range(1, N+1)}
    worm = {i:[] for i in range(1, N+1)}

    for _ in range(M):
        S, E, T = map(int, input().split())
        road[S].append((T, E))
        road[E].append((T, S))
    
    ws = set()
    we = set()
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        worm[S].append((T, E))
        ws.add(S)
        we.add(E)

    wst = [[1e9 for _ in range(N+1)] for _ in range(N+1)]
    for e in we:
        que = [(0, e)]
        visited = [1e9 for _ in range(N+1)]

        while que:
            t, v = heappop(que)
            for nxt_t, nxt_v in road[v]:
                new_t = t + nxt_t
                if visited[nxt_v] <= new_t:
                    continue
                
                visited[nxt_v] = new_t
                heappush(que, (nxt_t, nxt_v))
                if nxt_v in ws:
                    wst[e][nxt_v] = min(new_t, wst[e][nxt_v])
    
    for i in wst:
        print(i)
