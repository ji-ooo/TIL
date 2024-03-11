import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    # b.sort()
    cnt = 0
    # print(a, b)
    for i in range(B):
        start = 0
        end = A-1
        cur = b[i]
        while start <= end:
            mid = (start+end)//2
            if b[i] < a[mid]:
                end = mid - 1
            elif b[i] >= a[mid]:
                start = mid + 1
            # print(b[i], start, end, mid)
        cnt += A-start
        # print(cnt)
        # print('-----')
    print(cnt)