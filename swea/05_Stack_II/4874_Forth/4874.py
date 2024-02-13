import sys
sys.stdin = open('4874.txt')


# forth 계산할 함수
def forth_cal(line):
    # 빈 스택 생성, 숫자 저장
    forth = []
    # 입력받은 값 i로 순회
    for i in line:
        # i가 +, -, *, / 안에 있을 경우
        if i in ['+', '-', '*', '/']:
            # 저장된 숫자가 2개 이상일 경우에만 계산 진행
            if len(forth) >= 2:
                a, b = forth[-2], forth[-1]
                if i == '+':
                    forth[-2] = a + b
                elif i == '-':
                    forth[-2] = a - b
                elif i == '*':
                    forth[-2] = a * b
                elif i == '/':
                    forth[-2] = a // b
                forth.pop()
            # 2개보다 작다면 error 반환
            else:
                return 'error'
        # i가 .일 경우, forth에 저장된 수가 1일 때만 제대로 된 식
        elif i == '.':
            if len(forth) == 1:
                # 하나만 있을때 있는 값 반환
                return forth[0]
            else:
                # 하나가 아니라면 error 반환
                return 'error'

        else:
            forth.append(int(i))


T = int(input())
for tc in range(1, T+1):
    line = list(map(str, input().split()))

    result = forth_cal(line)
    print(f'#{tc} {result}')
