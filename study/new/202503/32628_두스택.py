import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
brr = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    arr[i] += arr[i - 1]
    brr[i] += brr[i - 1]

ans = max(arr[-1], brr[-1])

for k in range(max(0, N - K), min(N, 2 * N - K) + 1):
    ans = min(max(arr[k], brr[2 * N - K - k]), ans)

print(ans)