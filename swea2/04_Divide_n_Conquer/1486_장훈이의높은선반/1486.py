import sys
sys.stdin = open('1486.txt')


def top(idx, s):
    global result

    if B <= s:
        result = min(result, s)
        return
    if s > result:
        return

    if idx == N-1:
        return

    top(idx+1, s + h[idx+1])
    top(idx+1, s)


for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    h = list(map(int, input().split()))

    result = sum(h)
    for i in range(N):
        top(i-1, 0)
    print(f'#{tc} {result - B}')