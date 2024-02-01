from collections import deque

import sys
sys.stdin = open('4843.txt')


def bubble_sort(arr):
    l = len(arr)
    for i in range(l-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return deque(arr)


def counting_sort(arr):
    l = len(arr)
    std_arr = [0 for _ in range(l)]
    cnt_arr = [0 for _ in range(101)]

    for i in arr:
        cnt_arr[i] += 1
    for j in range(1, 101):
        cnt_arr[j] += cnt_arr[j-1]

    for k in range(l):
        index = arr[k]
        cnt_arr[index] -= 1
        std_arr[cnt_arr[index]] = index

    return deque(arr)


def selection_sort(arr):
    l = len(arr)
    for i in range(l):
        minIdx = i
        for j in range(i+1, l):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return deque(arr)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr = selection_sort(arr)

    result = ''
    for i in range(10):
        if i % 2 == 0:
            result += str(arr.pop())
        else:
            result += str(arr.popleft())
        result += ' '
    result = result[:-1]
    print(f'#{tc} {result}')

