import sys
sys.stdin = open('4865.txt')

T = int(input())
for tc in range(1, T+1):
    s1 = list(map(str, input()))
    s2 = str(input())

    cnt = {}
    for p in s1:
        cnt[p] = 0

    for p in cnt:
        for f in s2:
            if p == f:
                cnt[p] += 1

    print(f'#{tc} {max(cnt.values())}')
    # result = 0
    # for p in s1:
    #     result = max(result, s2.count(p))
    #
    # print(f'#{tc} {result}')
