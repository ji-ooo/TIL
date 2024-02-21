import sys
sys.stdin = open('5688.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N == 1:
        print(f'#{tc} {1}')
    else:
        start = 2
        end = int(N**(1/3))+1

        d = []
        for i in range(start, end + 1):
            if N % i == 0:
                d.append(i)

        result = -1
        for i in d:
            if N%(i**2) == 0 and i**3 == N:
                result = i
                break

        print(f'#{tc} {result}')
