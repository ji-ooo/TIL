import sys
sys.stdin = open('4839.txt')

# 이진탐색 함수
def binarysearch(start, end, key):
    # 세는 횟수, 1부터 시작
    cnt = 1
    # 시작, 끝 조건 설정
    while start <= end:
        middle = (start+end)//2
        if key > middle:
            start = middle
            cnt += 1
        elif key < middle:
            end = middle
            cnt += 1
        else:
            return cnt


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    left = 1
    right = P

    a_cnt = binarysearch(left, right, A)
    b_cnt = binarysearch(left, right, B)
    
    # 찾으려는 페이지가 최대 페이지보다 클 경우 제외
    if A > P:
        a_cnt = 1000
    if B > P:
        b_cnt = 1000
    
    # a와 b 횟수 비교, 출력
    if a_cnt < b_cnt:
        print(f'#{tc} A')
    elif a_cnt > b_cnt:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
