N = int(input())
find = int(input())
arr = [[0] * N for _ in range(N)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

num = 1
center = N // 2
current = (center, center)

d = 2
turn_check = 2
turn_cnt = 0
turn = 0
while num <= N ** 2:
    x, y = current
    if num == find:
        ansx, ansy = x+1, y+1
    if num == 1:
        arr[x][y] = 1
        x -= 1
        current = x, y
        num += 1

    elif num == 2:
        arr[x][y] = 2
        y += 1
        current = x, y
        num += 1

    elif num == 3:
        arr[x][y] = 3
        x += 1
        current = x, y
        num += 1

    else:
        arr[x][y] = num
        turn_cnt += 1
        if turn_cnt == turn_check:
            turn_cnt = 0
            turn += 1
            if turn % 2 == 0:
                turn_check += 1

            d += 1
            if d == 4:
                d = 0

        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            current = nx, ny
        num += 1

for i in range(N):
    print(*arr[i])
print(ansx, ansy)



