import sys
sys.stdin = open('16268.txt')


def pop(row, col):
    # 꽃가루 갯수 저장
    flower = arr[row][col]
    # 함수 시작 지점은 탐색 x, 미리 더해줌
    balloon = flower
    # 델타 방향 설정
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # nx, ny 범위가 배열 내에 있으면 꽃가루 값 더해줌
    for dx, dy in directions:
        nx = row + dx
        ny = col + dy
        if 0 <= nx < N and 0 <= ny < M:
            balloon += arr[nx][ny]

    return balloon


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 최대 터트리는 갯수 저장
    max_pop = 0
    for row in range(N):
        for col in range(M):
            tmp = pop(row, col)

            max_pop = max(max_pop, tmp)

    print(f'#{tc} {max_pop}')