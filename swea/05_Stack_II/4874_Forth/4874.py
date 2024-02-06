import sys
sys.stdin = open('4874.txt')

from collections import deque


def forth_cal(line):
    forth = deque()
    for i in line:
        if i in {'+', '-', '*', '/'}:
            if len(forth) >= 2:
                a, b = forth.pop(), forth.pop()
                if i == '+':
                    forth.append(a + b)
                elif i == '-':
                    forth.append(a - b)
                elif i == '*':
                    forth.append(a * b)
                elif i == '/':
                    forth.append(a // b)
            else:
                return 'error'

        elif i == '.':
            if len(forth) == 1:
                return forth[0]
            else:
                return 'error'

        else:
            forth.append(int(i))


T = int(input())
for tc in range(1, T+1):
    line = list(map(str, input().split()))

    result = forth_cal(line)
    print(f'#{tc} {result}')
