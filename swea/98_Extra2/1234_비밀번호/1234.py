import sys
sys.stdin = open('1234.txt')

for tc in range(1, 11):
    N, pw = map(str, input().split())
    N = int(N)
    pw = list(map(int, pw))

    i = 0

    while i < len(pw)-1:
        if pw[i] == pw[i+1]:
            pw = pw[:i] + pw[i+2:]
            i -= 1
        else:
            i += 1

    pw = ''.join(list(map(str, pw)))
    print(f'#{tc} {pw}')
