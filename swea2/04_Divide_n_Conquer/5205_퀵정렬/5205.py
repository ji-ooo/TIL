import sys
sys.stdin = open('5205.txt')


def quick(arr):
    if len(arr) <= 1:
        return arr

    p = arr[0]
    left, right, mid = [], [], []
    for i in arr:
        if i < p:
            left.append(i)
        elif i > p:
            right.append(i)
        else:
            mid.append(i)

    return quick(left) + mid + quick(right)


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc} {quick(arr)[N // 2]}')
