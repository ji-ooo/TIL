import sys
sys.stdin = open('4881.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    mini = 0
    for m in range(N):
        mini += arr[m][m]

    print(mini)