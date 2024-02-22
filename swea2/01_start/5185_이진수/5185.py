import sys
sys.stdin = open('5185.txt')


for tc in range(1, int(input()) + 1):
    N, n = map(str, input().split())
    n = format(int(n, 16), 'b')
    while len(n)%4 != 0:
        n = '0' + n
    print(f'#{tc} {n}')
