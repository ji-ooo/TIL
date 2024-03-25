import sys
input = sys.stdin.readline

N = int(input())

result = 1
for _ in range(N):
    result += int(input()) -1
print(result)