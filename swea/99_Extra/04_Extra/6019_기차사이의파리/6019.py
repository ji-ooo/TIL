import sys
sys.stdin = open('6019.txt')

for tc in range(1, int(input()) + 1):
    D, A, B, F = map(int, input().split())
    c = D/(A+B)
    print(f'#{tc} {c*F}')