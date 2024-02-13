import sys
sys.stdin = open('2005.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N == 1:
        pascal = [[1]]
    else:
        pascal = [[1], [1, 1]]

    for i in range(2, N):
        line = [1]
        prev = pascal[i-1]
        for j in range(len(prev)-1):
            line.append(prev[j] + prev[j+1])
        line.append(1)
        pascal.append(line)
    print(f'#{tc}')
    for p in pascal:
        print(*p)