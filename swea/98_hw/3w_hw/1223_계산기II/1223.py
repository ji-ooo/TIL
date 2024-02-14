import sys
sys.stdin = open('1223.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    line = list(map(str, input()))
    # 후위연산으로 변경 후 저장할 cal, 임시 stack 생성
    cal = []
    stack = []

    for tkn in line:
        # 토큰이 사칙연산 중 하나라면
        if tkn in ['+', '-', '*', '/']:
            # 토큰이 + 이거나 - 일 경우
            if tkn == '+' or tkn == '-':
                # 우선순위가 가장 낮으므로,
                # 스택에 요소가 있다면 계속 pop => cal에 push
                while stack:
                    cal.append(stack.pop())
                # 스택이 비고 나면 토큰을 스택에 push
                stack.append(tkn)
            # 토큰이 *이거나 / 일 경우
            elif tkn == '*' or tkn == '/':
                # 스택이 있고, top 요소가 +, -일 때 까지
                # 스택 top 을 pop => cal에 push
                while stack and stack[-1] not in ('+', '-'):
                    cal.append(stack.pop())
                stack.append(tkn)
        # 숫자일 경우 바로 cal에 push
        else:
            cal.append(int(tkn))

    # stack에 남은 요소가 있다면 cal에 전부 push
    while stack:
        cal.append(stack.pop())

    # cal을 순회하면서, stack에 계산되는 값 저장
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
