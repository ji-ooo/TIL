import sys
sys.stdin = open('5202.txt')

for tc in range(1, int(input())+1):
    N = int(input())

    dic_t = {i:-1 for i in range(0, 25)}
    for _ in range(N):
        s, e = map(int, input().split())
        if dic_t[e]:
            if dic_t[e] < s:
                dic_t[e] = s
        else:
            dic_t[e] = s

    start = 0
    end = 1
    cnt = 0
    while end <= 24:
        if dic_t[end] == -1:
            end += 1
        else:
            if dic_t[end] >= start:
                cnt += 1
                start = end
                end += 1
            else:
                end += 1

    print(f'#{tc} {cnt}')
