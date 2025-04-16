from collections import deque

def sol(s, t):
    if s == t:
        return 0
    
    que = deque([(s, '')])
    visited = {s}

    op = [
        ('*', lambda x: x * x),
        ('+', lambda x: x + x),
        ('-', lambda x: 0),
        ('/', lambda x: 1 if x !=- 0 else None)
    ]
    
    while que:
        now, path = que.popleft()

        for i, cal in op:
            if i == '/' and now == 0:
                continue

            new = cal(now)

            if new <= 1e9:
                if new == t:
                    return path + i
                
                if new not in visited:
                    visited.add(new)
                    que.append((new, path + i))

    return -1

s, t = map(int, input().split())
print(sol(s, t))