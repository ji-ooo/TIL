N = int(input())

arr = [0 for _ in range(1005)]

arr[1] = 1
arr[2] = 2

for i in range(1, 1001):
    if arr[i] == 1:
        arr[i+1] = 2
        arr[i+3] = 2
    else:
        arr[i+1] = 1
        arr[i+3] = 1

if arr[N] == 1:
    print('SK')
else:
    print('CY')
