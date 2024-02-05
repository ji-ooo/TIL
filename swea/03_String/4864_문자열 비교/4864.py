import sys
sys.stdin = open('4864.txt')

T = int(input())
for tc in range(1, T+1):
    find = str(input())
    word = str(input())

    if find in word:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')