N = int(input())
arr = list(map(int, input().split()))

arr.sort()

arr = arr[N:2*N]
print(arr[-1]-arr[0])