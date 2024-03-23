import sys
sys.stdin = open('5209.txt')


def backtrack(row, s):
    global result

    # 현재 합이 지금까지 최소보다 크면 더 안보고 끝
    if s > result:
        return

    # 마지막 제품까지 왔으면 최소값 비교 후 return
    elif row == N:
        result = min(result, s)
        return

    # 공장을 하나씩 순회 하면서,
    for col in range(N):
        # 아직 물건이 안정해진 공장인지 판단
        if not visited[col]:
            # 방문처리 후
            visited[col] = 1
            # 재귀 호출
            backtrack(row+1, s + arr[row][col])
            # 방문처리 해제
            visited[col] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대 비용 99이므로 100*N부터 시작
    result = 100 * N
    visited = [0] * N
    # row, 합
    backtrack(0, 0)
    print(f'#{tc} {result}')