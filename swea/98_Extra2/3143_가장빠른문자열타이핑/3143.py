import sys
sys.stdin = open('3143.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())
    cnt = A.count(B)

    result = len(A) - cnt * (len(B)-1)
    print(f'#{tc} {result}')

