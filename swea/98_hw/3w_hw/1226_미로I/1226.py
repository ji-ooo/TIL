import sys
sys.stdin = open('1226.txt')

from collections import deque

# 테스트케이스 수, 델타탐색 방향
T = 10
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for t in range(1, T+1):
    tc = int(input())
    # 미로 받을 빈 배열
    arr = []
    # 시작점, 무조건 1, 1
    start = (1, 1)
    # 안된다고 가정하고 시작, 끝까지 도착 못하면 그대로 0 출력
    result = 0
    # 미로 배열 입력
    for i in range(16):
        line = list(map(int, input()))
        arr.append(line)

    # 방문 처리 할 2차원 배열 생성
    visited = [[False] * 16 for _ in range(16)]
    # 탐색을 위해 que 생성, 시작점 입력
    que = deque([start])
    # 다음 탐색할 칸이 있으면 계속
    while que:
        # 현재 탐색 지점 que에서 pop, v => x, y로 분리
        v = que.pop()
        x, y = v
        # 현재 탐색 지점 방문처리
        visited[x][y] = True

        # 델타탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 다음 탐색 목표 지점이 범위 안에 있고,
            # 갈 수 있는 땅(0)이고,
            # 방문 하지 않았다면
            # 다음 탐색을 위해 que에 저장
            if 0 <= nx < 16 and 0 <= ny < 16:
                if arr[nx][ny] == 0 and not visited[nx][ny]:
                    que.append((nx, ny))
                # 다음 탐색할 지점이 3이라면 도착, 더 이상 탐색 필요 없음.
                if arr[nx][ny] == 3:
                    result = 1
                    break
        # 도착 가능하다면 탐색 필요 X
        if result:
            break
    print(f'#{tc} {result}')