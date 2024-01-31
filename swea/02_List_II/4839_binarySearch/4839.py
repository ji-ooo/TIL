import sys
sys.stdin = open('4839.txt')


def binarysearch(start, end, key):
    cnt = 1
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

    if A > P:
        a_cnt = 1000
    if B > P:
        b_cnt = 1000

    if a_cnt < b_cnt:
        print(f'#{tc} A')
    elif a_cnt > b_cnt:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
