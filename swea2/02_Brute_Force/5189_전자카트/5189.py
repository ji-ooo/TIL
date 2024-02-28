import sys
sys.stdin = open('5189.txt')


def cost(cnt, now, tmp_sum):
    global result
    if result < tmp_sum:
        return

    if cnt == N:
        result = tmp_sum
        return

    if cnt == N - 1:
        cost(cnt + 1, 0, tmp_sum + arr[now][0])

    else:
        for i in range(1, N):
            if not visited[i] and i != now:
                visited[i] = 1
                cost(cnt + 1, i, tmp_sum + arr[now][i])
                visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 101*N
    visited = [False] * N
    cost(0, 0, 0)
    print(f'#{tc} {result}')
