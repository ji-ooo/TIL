N, M = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

def per(n, l):
    if len(l) == M:
        print(*l)
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                l.append(num[i])
                per(n+1, l)
                l.pop()
                visited[i] = 0


visited = [0 for _ in range(N)]
per(0, [])
'''
2 4 5

'''

