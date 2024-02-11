from collections import deque

'''
T = int(input())
ans = []
for _ in range(T):
    A, B = map(int, input().split())
    
    visited = [False for _ in range(10000)]
    visited[A] = ''
    que = deque([A])

    while que:
        num = que.popleft()
        cmd = visited[num]
        D = (num*2)%10000

        if not visited[D]:
            visited[D] = cmd + 'D'
            que.append(D)

        S = num - 1
        if S == -1:
            S = 9999

        if not visited[S] == 0:
            visited[S] = cmd + 'S' 
            que.append(S)

        NUM = str(num)
        while len(NUM) != 4:
            NUM = '0'+ NUM

        d1, d2, d3, d4 = map(int, NUM)
        
        L = ((d2 * 10 + d3) * 10 + d4) * 10 + d1
        
        if not visited[L]:
            visited[L] = cmd + 'L'
            que.append(L)

        R = ((d4 * 10 + d1) * 10 + d2) * 10 + d3
                
        if not visited[R]:
            visited[R] = cmd + 'R'
            que.append(R)

        if visited[B]:
            break
    print(visited[B])
'''
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    
    visited = [[0, ''] for _ in range(10000)]
    visited[A][0] = 1
    que = deque([(A, '')])

    while que:
        cur = que.popleft()
        num = cur[0]
        cmd = cur[1]
        
        num = str(num)
        while len(num) != 4:
            num = '0'+ num

        d1, d2, d3, d4 = map(int, num)

        num = ((d1 * 10 + d2) * 10 + d3) * 10 + d4
        
        D = (num*2)%10000

        if visited[D][0] == 0:
            visited[D][0] = 1
            visited[D][1] += cmd + 'D'
            que.append([D, cmd + 'D'])

        S = num - 1
        if S == -1:
            S = 9999

        if visited[S][0] == 0:
            visited[S][0] = 1    
            visited[S][1] += cmd + 'S'
            que.append([S, cmd + 'S'])
        
        L = ((d2 * 10 + d3) * 10 + d4) * 10 + d1
        
        if visited[L][0] == 0:
            visited[L][0] = 1
            visited[L][1] += cmd + 'L'
            que.append([L, cmd + 'L'])

        R = ((d4 * 10 + d1) * 10 + d2) * 10 + d3
                
        if visited[R][0] == 0:
            visited[R][0] = 1
            visited[R][1] += cmd + 'R'
            que.append([R, cmd + 'R'])

        if visited[B][0] == 1:
            break

    print(visited[B][1])