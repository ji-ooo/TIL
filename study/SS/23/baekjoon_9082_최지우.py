import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().strip()))]
    arr.append(list(input().strip()))

    for i in range(N):
        c = 0
        if arr[0][i] == 3:
            c = 1
        elif arr[0][i] == 0:
            c = 2
            
        if c:
            if i != 0:
                arr[1][i-1] = '*' if c == 1 else 'x'
            if i != N-1:
                arr[1][i+1] = '*' if c == 1 else 'x'
            arr[1][i] = '*' if c == 1 else 'x'
