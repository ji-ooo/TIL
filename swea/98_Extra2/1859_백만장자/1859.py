import sys
sys.stdin = open('1859.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    tmp_max = price[N-1]
    i = N-2
    result = 0
    while i >= 0:
        if price[i] <= tmp_max:
            result += (tmp_max - price[i])
        elif price[i] > tmp_max:
            tmp_max = price[i]
        i -= 1

    print(f'#{tc} {result}')
