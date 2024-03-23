import sys
sys.stdin = open('1805.txt')


def backtrack(row, p):
    global result

    if p <= result:
        return
    elif row == N:
        result = round(p, 6)

    for per in range(N):
        if not used[per]:
            used[per] = 1
            backtrack(row + 1, p * (arr[row][per])/100)
            used[per] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    used = [0] * N
    result = 0
    backtrack(0, 100)
    print(f"#{tc} {format(result, '.6f')}")
