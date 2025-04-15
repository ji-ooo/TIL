def sol(pos, m):
    npos = sorted([p for p in pos if p < 0])
    ppos = sorted([p for p in pos if p > 0], reverse=True)
    total = 0
    
    for i in range(0, len(npos), m):
        tmp = npos[i : i + m]
        if tmp:       
            far = -tmp[0]  
            total += far * 2  
    
    for i in range(0, len(ppos), m):
        tmp = ppos[i : i + m]
        if tmp:
            far = tmp[0]  
            total += far * 2  

    if npos and ppos:
        dist = max(abs(npos[0]), ppos[0])

    elif npos:
        dist = -npos[0]

    elif ppos:
        dist = ppos[0]
    
    total -= dist

    return total


n, m = map(int, input().split())
pos = list(map(int, input().split()))

print(sol(pos, m))