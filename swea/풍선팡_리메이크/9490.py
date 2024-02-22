import sys
sys.stdin = open('9490.txt')


def bal(x, y, c, balloon):
    # 꽃가루 갯수 저장
    flower = arr[x][y]
    if flower%2 == 0:
        directions = [(1, 0), (-1, 0), (0, 0), (0, 1), (0, -1)]

    else:
        directions = [(-1, -1), (1, 1), (0, 0), (-1, 1), (1, -1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if (nx, ny) not in p_list:
                balloon += arr[nx][ny]
                if c == 0:
                    p_list.append((nx, ny))

    if c == 0:
        if (flower%2 == balloon%2 == 0) or (flower%2 == balloon%2 == 1):
            max_p = 0
            for ii in range(N):
                for jj in range(M):
                    t = bal(ii, jj, 1, balloon)
                    max_p = max(max_p, t)
            balloon = max_p
    t = 0
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
            p_list = []
            tmp = bal(i, j, 0, 0)
            max_pop = max(max_pop, tmp)

    print(f'#{tc} {max_pop}')