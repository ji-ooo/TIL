N = int(input())

if N == 0:
    print('NO')
else:
    th = [3**i for i in range(40)]
    for i in range(40-1, -1, -1):
        if N >= th[i]:
            N -= th[i]
        if N == 0:
            break
        
    if N > 0:
        print('NO')
    else:
        print('YES')