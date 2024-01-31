import sys
sys.stdin = open('Flatten.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    line = list(map(int, input().split()))
    line.sort()

    # 이동횟수가 남은 동안
    while N > 0:
        # 가장 낮은거 +1, 가장 낮은거 -1
        # 이동횟수 -1, 재정렬
        line[0] += 1
        line[-1] -= 1
        N -= 1
        line.sort()

    print(f'#{tc} {line[-1]-line[0]}')





























