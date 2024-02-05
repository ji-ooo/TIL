import sys
sys.stdin = open('9490.txt')


def pop(row, col):
    # 꽃가루 갯수 저장
    flower = arr[row][col]
    # -flower부터 +flower까지 가로, 세로 탐색하므로 가운데는 두번 저장
    # 미리 -flower 해주고 시작
    balloon = -flower
    
    # x범위 내 꽃가루 갯수 더함
    for x in range(-flower, flower+1):
        nx = row + x
        if 0 <= nx < N:
            balloon += arr[nx][col]
    # y범위 내 꽃가루 갯수 더함
    for y in range(-flower, flower+1):
        ny = col+y
        if 0 <= ny < M:
            balloon += arr[row][ny]

    return balloon


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # 최대값 저장
    max_pop = 0
    for row in range(N):
        for col in range(M):
            tmp = pop(row, col)

            max_pop = max(max_pop, tmp)

    print(f'#{tc} {max_pop}')