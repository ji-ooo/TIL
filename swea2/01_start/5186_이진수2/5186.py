import sys
sys.stdin = open('5186.txt')


for tc in range(1, int(input()) + 1):
    n = float(input())
    # n = format(n, 'b')
    i = 1
    output = ''
    while n > 0:
        b = 2**(-i)
        if n >= b:
            n -= b
            output += '1'
        else:
            output += '0'
        i += 1
        if len(output) > 12:
            output = 'overflow'
            break
    print(f'#{tc} {output}')
