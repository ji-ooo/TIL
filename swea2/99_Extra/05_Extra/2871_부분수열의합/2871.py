import sys
sys.stdin = open('2871.txt')


def backtrack(start, total, cnt):
    global result

    if total == K:
        result += 1
        return

    if cnt == K:
        return

    if start == N:
        return

    backtrack(start + 1, total + A[start], cnt + 1)
    backtrack(start + 1, total, cnt)


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = 0
    backtrack(0, 0, 0)
    print(f'#{tc} {result}')
