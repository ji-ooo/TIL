import sys
sys.stdin = open('4861.txt')


def find_x(i, j):
    word = arr[i][j:j+M]
    return word


def find_y(i, j):
    word = []
    for char in range(i, i+M):
        word.append(arr[char][j])
    return word


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = []
    result = []
    for _ in range(N):
        line = list(map(str, input()))
        arr.append(line)
    for i in range(N):
        for j in range(N):
            x = y = 0
            if j <= N-M:
                x = find_x(i, j)

                for k in range(M//2):
                    if x[k] != x[M-k-1]:
                        break
                else:
                    result = x
            if i <= N-M:
                y = find_y(i, j)

                for k in range(M//2):
                    if y[k] != y[M-k-1]:
                        break
                else:
                    result = y

            if result:
                break
    result = ''.join(result)
    print(f'#{tc} {result}')
