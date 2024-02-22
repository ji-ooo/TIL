import sys
sys.stdin = open('10580.txt')
# from collections import deque

for tc in range(1, int(input())+1):
    N = int(input())
    line = []
    for _ in range(N):
        A, B = map(int, input().split())
        line.append((A, B))
    line.sort(key=lambda x: -x[0])
    cnt = 0
    while line:
        current = line.pop()
        a, b = current

        for i in range(len(line)-1, -1, -1):
            if line[i][1] < b:
                cnt += 1
    print(f'#{tc} {cnt}')