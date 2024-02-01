import sys
sys.stdin = open('1954.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # N*N 빈 배열 생성
    arr = [[0]*N for _ in range(N)]

    # 숫자 채워나가는 방향대로 미리 델타 설정
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 시작 위치 0, 0 및 현재위치 업데이트 할 변수
    current = [0, 0]

    # 최초 방향 (0, 1) 설정, 진행 방향 direction 지정
    d = 0
    direction = directions[d]

    # 채울 숫자 및 시작 위치 1 채우기
    num = 1
    arr[0][0] = num

    # 마지막 값을 채우면 종료
    while num < N**2:
        # 현재 위치에서 x, y 추출
        x, y = current[0], current[1]

        # 델타 방향 지정
        dx, dy = direction[0], direction[1]

        # 다음 x, y 위치 지정
        nx = x + dx
        ny = y + dy

        # 다음 nx, ny가 범위 내에 있을 때
        if 0 <= nx < N and 0 <= ny < N:
            # 다음 nx, ny가 0일 경우
            # 숫자 +1, 배열에 넣고 현재 위치 업데이트
            if arr[nx][ny] == 0:
                num += 1
                arr[nx][ny] = num
                current = (nx, ny)
            # 아닐 경우 방향 변경
            # 방향이 4 일경우 한 바퀴 돌아 다시 0부터
            else:
                d += 1
                if d == 4:
                    d = 0
                direction = directions[d]
        # 다음 nx, ny가 범위를 벗어나도 방향 변경
        else:
            d += 1
            if d == 4:
                d = 0
            direction = directions[d]

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])