import sys
sys.stdin = open('5650.txt')

'''
블랙홀 -1: 닿으면 게임 끝남 최대 5개
웜홀 6 ~ 10: 반드시 한 쌍 주어짐, 닿으면 반대쪽 웜홀로, 방향 유지, 점수 X
블록 1~5: 1: 우상, 2: 우하, 3: 좌하, 4: 좌상 5: 네모

처음 위치로 돌아오거나 / 블랙홀에 빠지면 끝남
점수: 벽이나 블록에 부딪힌 횟수
출발점, 방향 임의 설정 가능 => 최대 값 구하기
'''


def start(v, d):
    x, y = v
    sx, sy = x, y

    score = 0
    m = 1
    route = []
    while True:
        dx, dy = ds[d]
        nx, ny = x + dx, y + dy
        route.append((x, y, d))
        print(route)
        print(f'x: {x}, y: {y}')
        print(f'sx: {sx}, sy: {sy}')
        print(f'nx: {nx}, ny:{ny}')
        now = arr[x][y]
        if 0 <= nx < N and 0 <= ny < N:
            b = arr[nx][ny]
            if b == -1:
                return score
            elif nx == sx and ny == sy:
                return score
            elif now in range(1, 6) and m == 1:
                d, m = turn(now, d, m)
                score += 1
                m = 0
            elif b == 0:
                x, y = nx, ny
            elif b in range(1, 6):
                d, m = turn(b, d, m)
                score += 1
                if m == 1:
                    x, y = nx, ny
                elif m == 2:
                    return score
            else:
                for w in warm[b]:
                    if w == (nx, ny):
                        continue
                    x, y = w
        else:
            # 밖에 나가는 경우 == 5번 만난 경우랑 똑같음
            b = 5
            d, m = turn(b, d, m)
            score += 1

            if m == 2:
                return score


td = {
    (0, 1): (1, 0), (0, 2): (1, 0), (0, 3): (2, 1), (0, 4): (3, 1), (0, 5): (1, 0),
    (1, 1): (3, 1), (1, 2): (2, 1), (1, 3): (0, 0), (1, 4): (0, 0), (1, 5): (0, 0),
    (2, 1): (0, 1), (2, 2): (3, 0), (2, 3): (3, 0), (2, 4): (1, 1), (2, 5): (3, 0),
    (3, 1): (2, 0), (3, 2): (0, 1), (3, 3): (1, 1), (3, 4): (2, 0), (3, 5): (2, 0)
      }


def turn(b, d, m):
    new_d, new_m = td[(d, b)]
    # m = 0 을 두번 연속으로 만나면 끝내야 함
    if new_m == 0 and m == 0:
        new_m = 2
    return new_d, new_m

'''
d = 0 : 우 / 1, 2, 5 => 1, 0 // 3 => 2, 1 // 4 => 3, 1
d = 1 : 좌 / 3, 4, 5 => 0, 0 // 1 => 3, 1 // 2 => 2, 1 
d = 2 : 하 / 2, 3, 5 => 3, 0 // 1 => 0, 1 // 4 => 1, 1
d = 3 : 상 / 1, 4, 5 => 2, 0 // 2 => 0, 1 // 3 => 1, 1
'''

ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for tc in range(1, int(input())+1):
    N = int(input())
    arr = []
    warm = {i: [] for i in range(6, 11)}
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if 6 <= line[j] <= 10:
                warm[line[j]].append((i, j))

        arr.append(line)

    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for d in range(4):
                    print(start((i, j), d))
                    # result = max(start((i, j), d), result)

    # print(result)
