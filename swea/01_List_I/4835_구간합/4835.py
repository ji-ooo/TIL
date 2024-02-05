import sys
sys.stdin = open('4835.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    line = list(map(int, input().split()))

    maxi = 0 # 구간합 최대 저장
    mini = 1e9 # 구간합 최소 저장
    # N-M+1번 순회하면서 M크기만큼 슬라이싱, tmp에 구간합 저장
    # maxi, mini에 최대 및 최소 저장
    for i in range(N-M+1):
        tmp = sum(line[i:i+M])
        maxi = max(maxi, tmp)
        mini = min(mini, tmp)

    print(f'#{tc} {maxi-mini}')