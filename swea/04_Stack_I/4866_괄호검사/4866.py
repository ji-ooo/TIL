import sys
sys.stdin = open('4866.txt')

T = int(input())
for tc in range(1, T+1):
    code = str(input())
    # 괄호 검사 할 빈 스택 생성
    bracket = []
    result = 0
    # 코드 문자열로 순회
    for i in code:
        # i가 여는 괄호일 경우 스택에 push
        if i == '(' or i == '{':
            bracket.append(i)
        # 닫는 괄호일 경우 스택의 top과 비교,
        # 쌍이 맞으면 pop, 아니면 순회 멈춤
        elif i == ')':
            if bracket and bracket[-1] == '(':
                bracket.pop()
            else:
                break
        elif i == '}':
            if bracket and bracket[-1] == '{':
                bracket.pop()
            else:
                break
    # 멈추지 않고 끝까지 순회 했을 때
    # == 닫는 괄호에 대해서 쌍이 전부 맞았을 때
    # 남은 여는 괄호가 남아 있지 않다면, 제대로 된 괄호
    else:
        if not bracket:
            result = 1

    print(f'#{tc} {result}')

'''
T = int(input())
for tc in range(1, T+1):
    code = str(input())

    bracket = []

    for i in code:
        if i == '(':
            bracket.append(i)
        elif i == '{':
            bracket.append(i)
        elif i == ')':
            if bracket and bracket[-1] == '(':
                bracket.pop()
            else:
                result = 0
                break
        elif i == '}':
            if bracket and bracket[-1] == '{':
                bracket.pop()
            else:
                result = 0
                break

    if bracket:
        result = 0
    else:
        result = 1

    print(f'#{tc} {result}')



'''


