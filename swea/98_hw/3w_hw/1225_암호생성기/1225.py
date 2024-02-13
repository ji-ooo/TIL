import sys
sys.stdin = open('1225.txt')

from collections import deque

for tc in range(1, 11):
    T = int(input())
    num = list(map(int, input().split()))
    que = deque(num)

    while que[-1] != 0:
        for i in range(1, 6):
            n = que.popleft()

            if n-i > 0:
                n -= i
                que.append(n)
            else:
                que.append(0)
                break

    result = ' '.join(map(str, list(que)))
    print(f'#{T} {result}')