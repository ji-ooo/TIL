import sys
sys.stdin = open('1961.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []
    ans_list = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
        ans_list.append([])

    for _ in range(3):
        for i in range(N):
            for j in range(N):
                if i < j:
                    arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

        for i in range(N):
            for j in range(N):
                if j < N//2:
                    arr[i][j], arr[i][N-j-1] = arr[i][N-j-1], arr[i][j]

        for x in range(N):
            ans_list[x] += arr[x]
            ans_list[x] += [' ']

    print(f'#{tc}')
    for i in range(N):
        print(''.join(map(str, ans_list[i])))
