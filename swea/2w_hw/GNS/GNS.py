import sys
sys.stdin = open('GNS.txt')

T = int(input())
for tc in range(1, T+1):
    t, N = map(str, input().split())
    N = int(N)
    line = list(map(str, input().split()))
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    numbers = dict()
    for i in num:
        numbers[i] = 0

    for n in line:
        numbers[n] += 1

    result = []
    for x in num:
        tmp = [x] * numbers[x]
        result.extend(tmp)
    print(f'#{tc}')
    print(*result)