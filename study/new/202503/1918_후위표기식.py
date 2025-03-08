eq = list(input())
stack = []
ans = []

for i in eq:
    if i == '(':
        stack.append(i)

    elif i in ('*', '/'):
        while stack and stack[-1] in ('*', '/'):
            ans.append(stack.pop())
        stack.append(i)

    elif i in ('+', '-'):
        while stack and stack[-1] != '(':
            ans.append(stack.pop())
        stack.append(i)

    elif i == ')':
        while stack and stack[-1] != '(':
            ans.append(stack.pop())
        stack.pop()

    else:
        ans.append(i)

while stack:
    ans.append(stack.pop())

print(''.join(ans))
