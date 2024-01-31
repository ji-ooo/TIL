import sys
sys.stdin = open('5789.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    cmd = []
    for _ in range(Q):
        cmd.append(list(map(int, input().split())))

    arr = [0] * N
    for i in range(Q):
        L, R = cmd[i]
        L -= 1
        for j in range(L, R):
            arr[j] = i+1

    result = ''
    for i in range(N):
        result += str(arr[i]) + ' '
    result = result[:-1]

    print(f'#{tc} {result}')
