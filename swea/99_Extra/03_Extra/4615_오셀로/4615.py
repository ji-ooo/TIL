import sys
sys.stdin = open('4615.txt')

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cmd = list(list(map(int, input().split()) for _ in range(M)))
    arr = [[0] * N for _ in range(N)]
    mid = N//2
    arr[mid-1][mid-1] = arr[mid][mid] = 2
    arr[mid][mid-1] = arr[mid-1][mid] = 1

    for x, y, color in cmd:
        x -= 1
        y -= 1
        if color == 1:
            arr[x][y] = 1

            for dx, dy in directions:
                change = [(x, y)]

                nx, ny = x + dx, y + dy
                while 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] == 2:
                        change.append((nx, ny))
                        nx += dx
                        ny += dy

                    elif arr[nx][ny] == 1:
                        for a, b in change:
                            arr[a][b] = 1
                        break
                    else:
                        break
        else:
            arr[x][y] = 2

            for dx, dy in directions:
                change = [(x, y)]

                nx, ny = x + dx, y + dy
                while 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] == 1:
                        change.append((nx, ny))
                        nx += dx
                        ny += dy

                    elif arr[nx][ny] == 2:
                        for a, b in change:
                            arr[a][b] = 2
                        break
                    else:
                        break
    white = black = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                white += 1
            elif arr[i][j] == 1:
                black += 1
    print(f'#{tc} {black} {white}')