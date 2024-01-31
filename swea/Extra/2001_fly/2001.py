import sys
sys.stdin = open('2001.txt')

def fly(x, y):
    find = 0
    for i in range(M):
        for j in range(M):
            find += arr[x+i][y+j]
    return find


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        line = list(map(int, input().split()))
        arr.append(line)

    max_fly = 0

    for x in range(N-M+1):
        for y in range(N-M+1):
            tmp = fly(x, y)
            max_fly = max(tmp, max_fly)

    print(f'#{tc} {max_fly}')
