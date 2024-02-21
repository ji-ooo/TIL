import sys
sys.stdin = open('input.txt')


# 백트래킹 함수, 현재 열과 임시 합을 인자로 받음
def backtrack(row, tmp_sum):
    # 최소값 global 선언
    global mini
    # 최소값보다 임시 합이 클 경우 탐색 중단
    if mini <= tmp_sum:
        return
    # 마지막 줄 까지 탐색 했을 경우 최소값 갱신
    # 위에서 큰지 비교 했기 때문에 바로 넣어도 됨
    elif row == N:
        mini = tmp_sum
    else:
        # 백트래킹
        # for 문으로 돌면서 모든 경우의 수 계산
        for col in range(N):
            if not visited[col][0]:
                visited[col][0] = 1
                backtrack(row + 1, tmp_sum + arr[row][col])
            elif not visited[col][1]:
                visited[col][1] = 1
                backtrack(row + 1, tmp_sum + arr[row][col])
                visited[col][1] = 0
            visited[col][0] = 0
            # 미리 방문처리 후 재귀 진행
            # 다음 열, 임시 합에 값 더해줌

            # 내부에서 할 수 있는 경우의 수 계산이 다 끝나면 방문처리 없앰
            # 다음 for 문 진행 시 방문할 수 있도록


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # 최소값 100으로 설정
    mini = 1e9
    # 행 체크할 리스트
    visited = [[0, 0]] * N

    # 열 0, 임시합 0으로 함수 실행
    backtrack(0, 0)

    print(f'#{tc} {mini}')
