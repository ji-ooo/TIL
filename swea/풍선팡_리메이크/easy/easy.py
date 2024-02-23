import sys
sys.stdin = open('input.txt')


def bal(x, y,):
    # 꽃가루 갯수 저장
    balloon = 0
    flower = arr[x][y]
    if flower%2 == 0:
        directions = [(1, 0), (-1, 0), (0, 0), (0, 1), (0, -1)]

    else:
        directions = [(-1, -1), (1, 1), (0, 0), (-1, 1), (1, -1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            balloon += arr[nx][ny]

    return balloon


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # 최대값 저장
    max_pop = 0
    for i in range(N):
        for j in range(M):
            tmp = bal(i, j)
            max_pop = max(max_pop, tmp)

    print(f'#{tc} {max_pop}')