import sys
sys.stdin = open('4881.txt')


def backtrack(row, tmp_sum):
    global mini
    if tmp_sum >= mini:
        return
    elif row == N and tmp_sum < mini:
        mini = tmp_sum
    else:
        for col in range(N):
            if not visited[col]:
                visited[col] = 1
                backtrack(row+1, tmp_sum+arr[row][col])
                visited[col] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    mini = 0
    for m in range(N):
        mini += arr[m][m]
    visited = [0] * N
    backtrack(0, 0)

    print(f'#{tc} {mini}')
