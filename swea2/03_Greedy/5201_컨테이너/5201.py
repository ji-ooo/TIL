import sys
sys.stdin = open('5201.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort()
    t.sort()
    result = 0
    while t:
        tone = t.pop()
        while w:
            weight = w.pop()
            if tone >= weight:
                result += weight
                break

    print(f'#{tc} {result}')
