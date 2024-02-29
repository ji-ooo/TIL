import sys
sys.stdin = open('input.txt')


# 백트래킹 함수, 현재 row와 임시 합을 인자로 받음
def backtrack(row, tmp_sum):
    # 최소값 global 지정
    global mini

    # 최소값보다 지금까지의 임시 합이 클 경우 탐색 중단
    # 더 탐색할 필요가 없음
    if mini <= tmp_sum:
        return

    # 마지막 줄 까지 탐색 했을 경우 최소값 갱신
    # 위에서 작은 값이면 함수를 종료하므로 바로 갱신 해도 된다
    elif row == N:
        mini = tmp_sum

    else:
        # 백트래킹
        # for 문으로 돌면서 모든 경우의 수 계산
        for col in range(N):
            # 방문 할 때마다 방문 횟수 +1 해주고 재귀함수 호출
            # 방문 횟수가 2보다 작을때만
            if visited[col] < 2:
                visited[col] += 1
                backtrack(row+1, tmp_sum + arr[row][col])
                # 재귀함수를 빠져나오면서 방문횟수 -1을 해주어야 함
                visited[col] -= 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # 최소값 701으로 설정, 최대가 700이기 때문에
    mini = 701

    # col 방문 했는 지 체크할 리스트
    # 두 번까지 방문 가능
    visited = [0] * N
    # visited = [0, 0, 0]
    # row 0, 임시 합 0으로 함수 실행
    backtrack(0, 0)

    print(f'#{tc} {mini}')