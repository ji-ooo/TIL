T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    print(arr)