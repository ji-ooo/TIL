import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]

    score.sort()
    
    pre = score[0][1]
    cnt = 1
    for i in range(1, N):
        if pre > score[i][1]:
            pre = score[i][1]
            cnt += 1

    print(cnt)