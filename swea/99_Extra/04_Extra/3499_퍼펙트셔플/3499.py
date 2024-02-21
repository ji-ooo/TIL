import sys
sys.stdin = open('3499.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(str, input().split()))
    if N%2 == 0:
        left = cards[:N//2]
        right = cards[N//2:]
    else:
        left = cards[:N//2 + 1]
        right = cards[N//2 +1:]
    result = []
    for i in range(N):
        if i%2 == 0:
            result.append(left[i//2])
        else:
            result.append(right[i//2])
    print(f'#{tc} {" ".join(result)}')
