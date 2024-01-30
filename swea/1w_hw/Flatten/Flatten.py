import sys
sys.stdin = open('Faltten.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    line = list(map(int, input().split()))
    line.sort()

    cnt = 0
    start = 0
    end = 99

    while cnt < N:
        line[0] += 1
        line[-1] -= 1
        cnt += 1
        line.sort()

    print(f'#{tc} {line[-1]-line[0]}')





























