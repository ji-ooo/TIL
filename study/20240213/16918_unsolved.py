from collections import deque
import sys
input = sys.stdin.readline
R, C, N = map(int, input().split())

arr = []
for _ in range(R):
    line = list(map(str, input().strip()))
    arr.append(line)

que1 = deque([])
que2 = deque([])

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

ans = []
ans.append(arr)
arr2 = [['O']*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            que1.append((i, j))

current = 0
idx = 0
N %= 4
if N%2 == 0:
    for i in range(R):
        print(*arr2, end='')
elif N == 1:
    for i in range(R):
        print(arr, end='')
else:
    while idx < 4:
        idx += 1
        if current == 1:
            pass
        elif current%2 == 0:
            for i in range(R):
                for j in range(C):
                    if arr[i][j] == '.':
                        arr[i][j] = 'O'

        else:
            while que1:
                v = que1.pop()
                x, y = v
                if arr[x][y] == 'O':
                    arr[x][y] = '.'
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < R and 0 <= ny < C:
                            if arr[nx][ny] == 'O' and (nx, ny) not in que1:
                                arr[nx][ny] = '.'

# if N%2 == 0:
#     for i in range(R):
#         print(*ans[1][i])
# elif N == 3:
#     for i in range(R):
#         print(*ans[2][i])
# else:
#     for i in range(R):
#         print(*ans[0][i])
