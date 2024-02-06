A, K = map(int, input().split())

arr = [i for i in range(K+1)]

# arr[A] = 1
arr[A+1] = 1

if A*2 <= K:
    arr[A*2] = 1

if A+2 <= K:
    for i in range(A+2, K+1):
        if i%2 == 0:
            arr[i] = min(arr[i//2]+1, arr[i-1]+1, arr[i])
        else:
            arr[i] = min(arr[i-1]+1, arr[i])
        
    print(arr[K])
else:
    print(K-A)
