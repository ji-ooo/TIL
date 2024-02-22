import sys
sys.stdin = open('11315.txt')


def find_d(v):
    directions1 = [(-2, -2), (-1, -1), (1, 1), (2, 2)]
    directions2 = [(-2, 2), (-1, 1), (1, -1), (2, -2)]
    x, y = v

    for dx, dy in directions1:
        nx, ny = x + dx, y + dy
        if arr[nx][ny] != 'o':
            break
    else:
        return 1

    for dx, dy in directions2:
        nx, ny = x + dx, y + dy
        if arr[nx][ny] != 'o':
            break
    else:
        return 1
    return 0


def find_x(v):
    x, y = v
    directions = [(0, -2), (0, -1), (0, 1), (0, 2)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if arr[nx][ny] != 'o':
            break
    else:
        return 1
    return 0


def find_y(v):
    x, y = v
    directions = [(-2, 0), (-1, 0), (1, 0), (2, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if arr[nx][ny] != 'o':
            break
    else:
        return 1
    return 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    tmp = 0
    if tc == 5:
        tmp = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                if 2 <= i < N - 2 and 2 <= j < N-2:
                    tmp = find_d((i, j))
                if tmp: break

                if 2 <= j < N-2:
                    tmp = find_x((i, j))
                if tmp: break

                if 2 <= i < N-2:
                    tmp = find_y((i, j))
                if tmp: break
        if tmp: break

    result = 'NO'
    if tmp:
        result = 'YES'
    print(f'#{tc} {result}')