N = int(input())

arr = [1 for _ in range(1005)]

arr[2] = 2

for i in range(5, 1001):
    if arr[i-1] == arr[i-3] == arr[i-4] == 1:
        arr[i] = 2
    
if arr[N] == 1:
    print('SK')
else:
    print('CY')