import sys
sys.stdin = open('5204.txt')


def dq(arr):
    l = len(arr)
    if l <= 1:
        return arr

    mid = l//2
    left = dq(arr[:mid])
    right = dq(arr[mid:])

    return merge(left, right)


def merge(left, right):
    global cnt
    tmp = []
    if left[-1] > right[-1]:
        cnt += 1
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            tmp.append(left[l])
            l += 1
        else:
            tmp.append(right[r])
            r += 1

    while l < len(left):
        tmp.append(left[l])
        l += 1
    while r < len(right):
        tmp.append(right[r])
        r += 1

    return tmp


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    print(f'#{tc} {dq(arr)[N // 2]} {cnt}')
