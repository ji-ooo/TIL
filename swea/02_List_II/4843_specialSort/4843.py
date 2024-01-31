import sys
sys.stdin = open('4843.txt')

from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    arr = deque(arr)

    result = ''
    for i in range(10):
        if i%2 == 0:
            result += str(arr.pop())
        else:
            result += str(arr.popleft())
        result += ' '
    result = result[:-1]
    print(f'#{tc} {result}')

