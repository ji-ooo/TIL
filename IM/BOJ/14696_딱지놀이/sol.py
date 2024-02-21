import sys
sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    a, *A = map(int, input().split())
    a, *B = map(int, input().split())
    print(A, B)
    # for c in range(1, 5):
