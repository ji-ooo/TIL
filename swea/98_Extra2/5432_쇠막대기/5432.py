import sys
sys.stdin = open('5432.txt')

T = int(input())
for tc in range(1, T+1):
    razor = str(input())
    razor = razor.replace("()", "R")
    result = 0
    pipe = 0
    for i in razor:
        if i == '(':
            pipe += 1
        elif i == ')':
            pipe -= 1
            result += 1
        else:
            result += pipe

    print(f'#{tc} {result}')
    '''
    |(((||)(|)|))(|)
    
    () 나오면 레이저로 변환
    (   ) 안에 레이저 몇개 있는지 세고 (   ) 없애기
    하면 될거 같은데
    
    '''