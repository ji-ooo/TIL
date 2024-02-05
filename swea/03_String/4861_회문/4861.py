import sys
sys.stdin = open('4861.txt')


def find_x(i, j):
    word = arr[i][j:j+M]
    return word


def find_y(i, j):
    word = []
    for x in range(i, i+M):
        word.append(arr[x][j])
    return word


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = []
    result = []
    for _ in range(N):
        line = list(map(str, input()))
        arr.append(line)
    for i in range(N-M+1):
        for j in range(N-M+1):
            x = find_x(i, j)
            y = find_y(i, j)
            for k in range(M//2):
                if x[k] == x[-k-1]:
                    continue
            else:
                result = x

            for k in range(M//2):
                if y[k] == y[-k-1]:
                    continue
            else:
                result = y
    print(result)
