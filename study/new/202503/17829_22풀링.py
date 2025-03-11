import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [(0, 0), (0, 1), (1, 0), (1, 1)]


def pool(v):
    x, y = v
    num = []

    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        num.append(arr[nx][ny])
    
    num.sort()

    return num[-2]


while len(arr) > 1:
    new_arr = []
    for i in range(0, len(arr), 2):
        tmp = []
        for j in range(0, len(arr), 2):
            r = pool((i, j))
            tmp.append(r)
        new_arr.append(tmp)
    arr = new_arr

print(arr[0][0])