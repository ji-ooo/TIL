import sys
sys.stdin = open('5176.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # root = N // 2 + 1
    # t = 0
    # for i in range(N):
    #     if N - 2**i < 0:
    #         t = i-1
    #         break
    #
    # root_max = 2 ** t
    # right_cnt = root_max // 2 - 1
    # root_num = N - right_cnt if N - right_cnt < root_max else root_max
    #
    # mid_lst = [0, 2]
    # for i in range(1, t):
    #     for j in range(1, 2**i+1):
    #         mid_lst.append(j*4-2)
    # if N == 1:
    #     print(f"#{tc} {1} {1}")
    # else:
    #     mid = N//2
    #     ans = mid_lst[mid]
    #     print(f"#{tc} {root_num} {ans}")

