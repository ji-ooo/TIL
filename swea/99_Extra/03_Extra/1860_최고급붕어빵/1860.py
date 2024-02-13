import sys
sys.stdin = open('1860.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # N명, M초의 시간동안 K개 만듦
    arr = list(map(int, input().split()))
    arr.sort()

    cnt = 0

    start = 0
    waste = 0
    result = 'Possible'
    for p in range(len(arr)):
        end = arr[p]
        cnt += ((end - start + waste)//M) * K
        if end != start:
            waste = (end - start + waste) % M
            # waste 초기화 안하도록 해야함,,
        if p+1 > cnt:
            result = 'Impossible'
            break

        start = arr[p]

    print(f'#{tc} {result}')
