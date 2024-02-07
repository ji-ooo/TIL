import sys
sys.stdin = open('input.txt')

class Stack:
    # stack을 생성할 때 필요한 값이 있는데,
    # stack의 크기를 지정해야 한다.
    def __init__(self, size):
        self.size = size
        # 자료구조 stack을 list를 활용해서 구현
        self.data = [None] * size # 값이 없음을 나타내는 None
        self.top = -1 # 초기 값이 없으므로, top의 위치는 -1

    def push(self, item): # stack에 값 삽입 -> 삽입할 대상 item을 인자로 받음
        if self.is_full(): # stack이 가득 찼다면
            print('Stack is Full!')
        # 받아온 item을 내 data에 top번째 위치에 삽입
        else:
            self.top += 1 # top 위치 1 증가
            self.data[self.top] = item
    
    def get(self):
        return self.data[self.top]

    def __str__(self): # instance print 했을 때, stack안의 data를 바로 출력
        return f'{self.data}'
    
    def pop(self):
        if self.is_empty():
            print('Stack is Empty!')
        else:
            self.top -= 1
            return self.data[self.top + 1]
    
    def is_empty(self):
        # top이 -1을 가리키고 있다면 stack은 비었다
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        return self.size == self.top +1


# stack = Stack(100)
# for i in range(101):
#     stack.push(10)
# stack.push(124153)
# print(stack.size)
# print(stack.data)
# print(stack.top)
# print(stack.data)
# print(stack.top)
# print(stack.get())
# print(stack)
# print(stack.pop())
# print(stack.pop())

T = int(input())
for tc in range(1, T+1):
    bracket = input()
    # 모든 문자열을 조사
    stack = Stack(100)
    for char in bracket:
        if char == '(':
            stack.push(char)
        else:
            if not stack.is_empty():
                if stack.get() == '(':
                    stack.pop()
            else:
                print(f'#{tc} {False}')
                break
    else:
        if stack.top != -1:
            print(f'#{tc} {False}')
