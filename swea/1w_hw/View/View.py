import sys
sys.stdin = open('View.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    line = list(map(int, input().split()))
    # ans = 0
    # i = 2
    # while 2 <= i < N-2:
    #     tmp = line[i]
    #     tmp_list = line[i-2:i+3]
    #     if tmp == max(tmp_list):
    #         tmp_list.remove(tmp)
    #         ans += tmp - max(tmp_list)
    #         i += 3
    #     else:
    #         i += 1
    ans = 0
    for i in range(2, N-2):
        tmp = line[i]
        tmp_list = line[i-2:i+3]
        if tmp == max(tmp_list):
            tmp_list.remove(tmp)
            ans += tmp - max(tmp_list)

    print(ans)
