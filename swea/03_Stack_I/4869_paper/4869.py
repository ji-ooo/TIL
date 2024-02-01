import sys
sys.stdin = open('4869.txt')


def paper(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    else:
        return paper(N-1) + paper(N-2)*2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N//10
    result = paper(n)

    print(f'#{tc} {result}')