import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    p_que, n_que = [], []
    visited = [False]*1000001

    for i in range(k):
        c, n = input().split()
        if c == 'I':
            heapq.heappush(p_que, (int(n), i))
            heapq.heappush(n_que, (-int(n), i))
            visited[i] = True
        
        else:
            if n == '-1':
                while p_que and not visited[p_que[0][1]]:
                    heapq.heappop(p_que)
                if p_que:
                    visited[p_que[0][1]] = False
                    heapq.heappop(p_que)
            
            if n == '1':
                while n_que and not visited[n_que[0][1]]:
                    heapq.heappop(n_que)
                if n_que:
                    visited[n_que[0][1]] = False
                    heapq.heappop(n_que)
    
    while p_que and not visited[p_que[0][1]]:
        heapq.heappop(p_que)
    while n_que and not visited[n_que[0][1]]:
        heapq.heappop(n_que)
    
    if len(p_que) == 0 or len(n_que) == 0:
        print('EMPTY')
    else:
        print(-n_que[0][0], p_que[0][0])
