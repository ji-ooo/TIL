import sys
input = sys.stdin.readline

N, P = map(int, input().split())

m = [list(map(int, input().split())) for _ in range(N)]

guitar = [[] for _ in range(7)]

cnt = 0
for t in m:
    line, fret = t
    while guitar[line] and guitar[line][-1] > fret:
        guitar[line].pop()
        cnt += 1

    if guitar[line] and guitar[line][-1] == fret:
        continue
            
    else:
        guitar[line].append(fret)
        cnt += 1
print(cnt)