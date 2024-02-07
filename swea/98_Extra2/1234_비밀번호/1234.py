import sys
sys.stdin = open('1234.txt')


class Stack:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.top = -1

    def push(self, item):
        if self.isFull():
            pass
        else:
            self.top += 1
            self.data[self.top] = item

    def pop(self):
        if self.isEmpty():
            pass
        else:
            self.top -= 1
            return self.data[self.top + 1]

    def isEmpty(self):
        if self.top == -1:
            return True
        else: return False

    def isFull(self):
        return self.size == self.top+1

    def __str__(self):
        return f'{self.data}'


for tc in range(1, 11):
    N, pw = map(str, input().split())
    N = int(N)
    stack = Stack(101)
    pw = list(map(int, pw))
    for i in pw:
        if stack.top != -1:
            if stack.data[stack.top] == i:
                stack.pop()
            else:
                stack.push(i)
        else:
            stack.push(i)

    pw = ''.join(map(str, stack.data[:stack.top+1]))
    print(f'#{tc} {pw}')

    # i = 0
    #
    # while i < len(pw)-1:
    #     if pw[i] == pw[i+1]:
    #         pw = pw[:i] + pw[i+2:]
    #         i -= 1
    #     else:
    #         i += 1
    #
    # pw = ''.join(list(map(str, pw)))
    # print(f'#{tc} {pw}')
