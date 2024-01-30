import sys
sys.stdin = open('4828.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = list(map(int, input().split()))
    ans = max(line) - min(line)
    print(f'#{tc} {ans}')
