import sys
sys.stdin = open('4843.txt')


def bubble_sort(arr):  # 버블
    l = len(arr)
    for i in range(l-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def counting_sort(arr):  # 카운팅
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

    return arr


def selection_sort(arr):  # 선택
    l = len(arr)
    for i in range(l):
        mini = i
        for j in range(i+1, l):
            if arr[mini] > arr[j]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]

    return arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # bubble_sort(arr)
    # counting_sort(arr)
    selection_sort(arr)

    result = ''
    # 리스트 10까지만 정렬
    # i가 짝수이면 최대값, 홀수이면 최소값 pop 해서 결과에 저장
    for i in range(10):
        if i % 2 == 0:
            result += str(arr.pop())
        else:
            result += str(arr.pop(0))
        result += ' '

    # 공백 제거
    result = result[:-1]
    print(f'#{tc} {result}')

