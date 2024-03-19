import sys
input = sys.stdin.readline

K, N = map(int, input().split())
L = []

for _ in range(K):
    L.append(int(input()))

min = 1
max = max(L)

while min <= max:
    mid = (min + max) // 2
    ans = 0
    for i in L:
        ans += i // mid
    if ans >= N: min = mid + 1
    else: max = mid - 1
            
print(max)