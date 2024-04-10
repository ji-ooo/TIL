import sys
sys.stdin = open('1949.txt')
from collections import deque

dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def make_road(v, h, c, r):
    global result
    r.append(v)
    que = deque([(v, h, c, r)])
    while que:
        v, h, c, r = que.popleft()
        result = max(result, len(r))
        x, y = v
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if (nx, ny) not in r:
                    if c and arr[nx][ny] - K < h:
                        que.append(((nx, ny), min(arr[nx][ny], arr[x][y]-1), c-1, r + [(nx, ny)]))
                    if arr[nx][ny] < h:
                        que.append(((nx, ny), arr[nx][ny], c, r + [(nx, ny)]))


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = []
    H = 0
    for _ in range(N):
        line = list(map(int, input().split()))
        arr.append(line)
        H = max(H, max(line))

    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == H:
                make_road((i, j), arr[i][j], 1, [])
    print(f'#{tc} {result}')
    '''
    K만큼 한 땅만 깎을 수 있다.
    다음칸에서 최대 K 까지 내린 다음에 현재 칸보다 낮게 할 수 있으면
    현재칸 -1 까지 깎아놓고 다음 탐색 시작 하면 될거같음
    현재칸 -1보다 더 깎을 이유가 전혀 없다.
    완전탐색 기반으로 4방향 델타 탐색 하면서
    좌표랑 현재 칸의 높이(깎았으면 깎은 후 높이), 깎을 수 있는지 여부(1, 0)를 인자로해서
    f(v, h, c)를 돌릴까
    그러면 방문처리 할 배열을 같이 넘겨줘야 할 듯 => 경로 리스트? 딕셔너리? 를 만들어서 넘기기
    재귀는 한번만 해도 되겠다 (깎았는지 여부만 재귀로 체크하면 될듯)
    '''