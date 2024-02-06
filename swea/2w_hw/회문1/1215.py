import sys
sys.stdin = open('1215.txt')


def find(x, y):
    nx, ny = x + N, y + N
    cnt = 0
    if nx <= 8:
        for i in range(N//2):
            if arr[x+i][y] != arr[x+N-1-i][y]:
                break
        else:
            cnt += 1

    if ny <= 8:
        for j in range(N//2):
            if arr[x][y+j] != arr[x][y+N-1-j]:
                break
        else:
            cnt += 1

    return cnt


for tc in range(1, 11):
    N = int(input())
    arr = []
    for _ in range(8):
        arr.append(list(map(str, input())))
    result = 0
    for i in range(8):
        for j in range(8):
            result += find(i, j)
    print(f'#{tc} {result}')
