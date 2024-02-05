import sys
sys.stdin = open('4866.txt')

T = int(input())
for tc in range(1, T+1):
    code = str(input())

    bracket = []
    result = 0
    for i in code:
        if i == '(' or i == '{':
            bracket.append(i)
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
    else:
        if bracket:
            result = 0
        else:
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


