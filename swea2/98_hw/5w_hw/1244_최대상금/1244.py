import sys
sys.stdin = open('1244.txt')

for tc in range(1, int(input())+1):
    N, c = input().split()
    c = int(c)
    N = list(map(int, N))
    srt_N = N[:]
    srt_N.sort(reverse=True)
    st_N = set(N)

    pos = 0
    while c > 0:
        if pos == len(N)-1:
            if len(N) != len(st_N):
                result = N
            else:
                if c % 2 == 1:
                    N[-2], N[-1] = N[-1], N[-2]
                result = N
            break
        if N[pos] != srt_N[pos]:
            target = 0
            for i in range(len(N)-1, -1, -1):
                if N[i] == srt_N[pos] and N[pos] == srt_N[i]:
                    target = i
                    break
            else:
                for i in range(len(N) - 1, -1, -1):
                    if N[i] == srt_N[pos]:
                        target = i
                        break
            N[pos], N[target] = N[target], N[pos]
            c -= 1
        pos += 1
    if c == 0:
        result = N

    print(f'#{tc}', ''.join(map(str, result)))