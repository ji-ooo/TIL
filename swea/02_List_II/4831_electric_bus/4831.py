import sys
sys.stdin = open('4831.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))

    current = 0
    cnt = 0
    able = True

    while current < N:
        tmp_pos = current + K

        for move in range(tmp_pos, current, -1):
            if move in bus_stop:
                current = move
                cnt += 1
                break
            elif move == current + 1:
                able = False
                break

        if not able:
            cnt = 0
            break

        if N-K <= current:
            break

    print(f'#{tc} {cnt}')
