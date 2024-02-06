import sys
sys.stdin = open('4865.txt')

T = int(input())
for tc in range(1, T+1):
    s1 = list(map(str, input()))
    s2 = str(input())

    result = 0
    # s1을 순회하면서, s2.count와 결과에 저장된 최대값 중
    # 큰 값을 결과에 저장
    for p in s1:
        result = max(result, s2.count(p))

    print(f'#{tc} {result}')
    # cnt = {}
    # for p in s1:
    #     cnt[p] = 0
    #
    # for p in cnt:
    #     for f in s2:
    #         if p == f:
    #             cnt[p] += 1
    #
    # print(f'#{tc} {max(cnt.values())}')
