import sys
sys.stdin = open('6485.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_list = [0 for i in range(0, 5001)]

    for _ in range(N):
        start, end = map(int, input().split())
        for i in range(start, end + 1):
            bus_list[i] += 1

    P = int(input())
    result = []
    for _ in range(P):
        c = int(input())
        result.append(bus_list[c])

    ans = ''
    for i in range(len(result)):
        ans += str(result[i]) + ' '
    ans = ans[:-1]
    print(f'#{tc} {ans}')
