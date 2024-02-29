import sys
sys.stdin = open('input.txt')


# 백트래킹 함수, 현재 열과 임시 합을 인자로 받음
def backtrack(row, tmp_sum):
    # 최소값 global 선언
    global mini
    global special
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
        if row in special:
            backtrack(row+1, tmp_sum + min(arr[row]))
        else:
            for col in range(N):
                # 방문한 적 없는 행이라면,
                if not visited[col]:
                    # 미리 방문처리 후 재귀 진행
                    # 다음 열, 임시 합에 값 더해줌
                    visited[col] = 1
                    backtrack(row+1, tmp_sum + arr[row][col])
                    # 내부에서 할 수 있는 경우의 수 계산이 다 끝나면 방문처리 없앰
                    # 다음 for 문 진행 시 방문할 수 있도록
                    visited[col] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    special = list(map(lambda x: int(x)-1, input().split()))
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # 최소값 100으로 설정
    mini = 101
    # 행 체크할 리스트
    visited = [0] * N
    # 열 0, 임시합 0으로 함수 실행
    backtrack(0, 0)

    print(f'#{tc} {mini}')
