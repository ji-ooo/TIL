import sys
input = sys.stdin.readline
N = int(input())
a, b, c = map(int, input().split())
A, B, C = a, b, c

for i in range(1, N):
    x, y, z = map(int, input().split())
    A, B, C = x + max(A, B), y + max(A, B, C), z + max(B, C)
    a, b, c = x + min(a, b), y + min(a, b, c), z + min(b, c)

print(max(A, B, C), min(a, b, c))