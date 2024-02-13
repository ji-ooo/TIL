import sys
sys.stdin = open('1234.txt')


# 스택 class
class Stack:
    # 스택 초기화 및 크기, top 위치 설정
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.top = -1

    # 스택이 가득 차있지 않다면 스택 맨위에 item 추가
    def push(self, item):
        if self.isFull():
            pass
        else:
            self.top += 1
            self.data[self.top] = item

    # 스택이 비어있지 않다면 스택 맨위의 값 반환
    def pop(self):
        if self.isEmpty():
            pass
        else:
            self.top -= 1
            return self.data[self.top + 1]

    # 스택이 비었는지 확인, top 위치가 -1일 때
    def isEmpty(self):
        if self.top == -1:
            return True
        else: return False

    # 스택이 가득 찼는지 확인, top 위치가 스택 크기와 같을 때
    def isFull(self):
        return self.size == self.top+1


for tc in range(1, 11):
    N, pw = map(str, input().split())
    N = int(N)
    # 100자 이하의 문자열 입력, 101크기의 스택 생성
    stack = Stack(101)

    # pw 순회
    for i in pw:
        # 스택이 비어있지 않다면
        if stack.top != -1:
            # 스택의 top 값과 i비교,
            # 같다면 pop, 다르면 push
            if stack.data[stack.top] == i:
                stack.pop()
            else:
                stack.push(i)
        # 스택이 비어있다면 push
        else:
            stack.push(i)

    pw = ''.join(stack.data[:stack.top+1])
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
