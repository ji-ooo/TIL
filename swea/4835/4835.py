import sys
sys.stdin = open('4835.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    line = list(map(int, input().split()))
    maxi = 0
    mini = 1e9
    for i in range(N-M+1):
        tmp = sum(line[i:i+M])
        maxi = max(maxi, tmp)
        mini = min(mini, tmp)

    print(f'#{tc} {maxi-mini}')