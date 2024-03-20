import sys
sys.stdin = open('5658.txt')
from collections import deque

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    n = list(str(input()))
    l = N//4
    num_lst = set()
    for i in range(l):
        for j in range(4):
            num_lst.add(int(''.join(n[l*j:l*(j+1)]), 16))
        que = deque(n)
        que.append(que.popleft())
        n = list(que)
    num_lst = sorted(list(num_lst), reverse=True)
    print(f'#{tc} {num_lst[K - 1]}')
