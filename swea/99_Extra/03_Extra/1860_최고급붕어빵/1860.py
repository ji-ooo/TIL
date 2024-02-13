import sys
sys.stdin = open('1860.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # N명, M초의 시간동안 K개 만듦
    arr = list(map(int, input().split()))
    arr.sort()
    cnt = 0
    t = 0
    while True:
        t += 1
        if t == M:
            cnt += K
