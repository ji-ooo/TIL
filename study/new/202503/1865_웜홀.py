import sys
input = sys.stdin.readline

TC = int(input())


def bellman(N):
    dist = [1e9] * (N + 1)
    dist[1] = 0

    for _ in range(N-1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
            
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return True
        
    return False


for tc in range(TC):
    N, M, W = map(int, input().split())
    edges = []

    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))
    
    print("YES" if bellman(N) else "NO")