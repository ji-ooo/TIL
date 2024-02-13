import sys
sys.stdin = open('1223.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    line = list(map(str, input()))
    cal = []
    stack = []
    for tkn in line:
        if tkn in ['+', '-', '*', '/']:
            if tkn == '+' or tkn == '-':
                while stack:
                    cal.append(stack.pop())
                stack.append(tkn)
            elif tkn == '*' or tkn == '/':
                while stack and stack[-1] not in ('+', '-'):
                    cal.append(stack.pop())
                stack.append(tkn)
        else:
            cal.append(int(tkn))
    while stack:
        cal.append(stack.pop())

    for i in cal:
        if i == '+':
            tmp = stack.pop() + stack.pop()
        elif i == '-':
            tmp = stack.pop() - stack.pop()
        elif i == '*':
            tmp = stack.pop() * stack.pop()
        elif i == '/':
            tmp = stack.pop() / stack.pop()
        else:
            tmp = i
        stack.append(tmp)
    print(f'#{tc} {stack[0]}')
