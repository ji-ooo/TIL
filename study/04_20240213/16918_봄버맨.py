from collections import deque
from copy import deepcopy
R, C, N = map(int, input().split())

arr = []
for _ in range(R):
    line = list(map(str, input().strip()))
    arr.append(line)

arr2 = deepcopy(arr)
arr = [['O']*C for _ in range(R)]

if N%2 == 0:
    for i in arr:
        print(''.join(i))

elif N == 1:
    for i in arr2:
        print(''.join(i))

else:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    que = deque([])
    for i in range(R):
        for j in range(C):
            if arr2[i][j] == 'O':
                que.append((i, j))

    while que:
        v = que.pop()
        x, y = v
        arr[x][y] = '.'
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                arr[nx][ny] = '.'
    if N%4 == 3:
        for i in arr:
            print(''.join(i))

    else:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O':
                    que.append((i, j))
        arr = [['O']*C for _ in range(R)]
        
        while que:
            v = que.pop()
            x, y = v
            arr[x][y] = '.'
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    arr[nx][ny] = '.'
        for i in arr:
            print(''.join(i))