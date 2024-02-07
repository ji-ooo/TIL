import sys
sys.stdin = open('4874.txt')


def forth_cal(line):
    forth = []
    for i in line:
        if i in {'+', '-', '*', '/'}:
            if len(forth) >= 2:
                a, b = forth[-2], forth[-1]
                if i == '+':
                    forth[-2] = a + b
                elif i == '-':
                    forth[-2] = a - b
                elif i == '*':
                    forth[-2] = a * b
                elif i == '/':
                    if b != 0:
                        forth[-2] = a // b
                    else:
                        return 'error'
                forth.pop()
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
