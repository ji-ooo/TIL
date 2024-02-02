import sys
sys.stdin = open('Sum.txt')

T = 10
for tc in range(1, T + 1):
    t = int(input())
    # 2차원 배열, 최대 합 저장할 변수 지정
    arr = []
    max_sum = 0

    # 행 입력 받으면서 배열에 추가, 행 마다 합을 구해서 최대 합과 비교 후 저장
    for _ in range(100):
        line = list(map(int, input().split()))
        arr.append(line)
        max_sum = max(max_sum, sum(line))

    # 열, 대각선 합 구하면서 최대 합과 비교 후 저장
    tmp_cross = 0
    tmp_rev_cross = 0
    for i in range(100):
        tmp_y = 0
        tmp_cross += arr[i][i]
        tmp_rev_cross += arr[i][99-i]
        for j in range(100):
            tmp_y += arr[j][i]
        max_sum = max(max_sum, tmp_y)
    max_sum = max(max_sum, tmp_cross, tmp_rev_cross)

    print(f'#{tc} {max_sum}')
