import sys
sys.stdin = open('9386.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = str(input())

    result = 0
    for i in range(N):
        if num[i] == '1':
            j = i+1
            while j < N:
                if num[j] == '1':
                    j += 1
                else:
                    break
            result = max(result, j-i)
    print(f'#{tc} {result}')