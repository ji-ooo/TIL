import sys
sys.stdin = open('input.txt')

C, R = map(int, input().split())
K = int(input())

cnt = 0
while True:
    if R == 1 or C == 1:
        break
    else:
        K -= 2*R + 2*C - 4
        R -= 2
        C -= 2
        cnt += 1

print(K, R, C, cnt)
arr = [[0] * C for _ in range(R)]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

now = (0, 0)
d = 0
if K == 1:
    x, y = 1, 1
else:
    while K > 0:
        x, y = now
        arr[x][y] = K
        
        dx, dy = directions[d]
        nx, ny = x+dx, y+dy

        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == 0:
            arr[nx][ny] = K
            K -= 1
            now = (nx, ny)
        else:
            d += 1
            if d == 4:
                d = 0
    print(y+1, x+1)
'''
100
99
99
98
98
97
97
96
'''