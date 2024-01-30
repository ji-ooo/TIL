N = int(input())
arr = [1]
arr.extend(list(map(int, input().split())))
arr.append(int(1e9))

cnt = 3
result = []
able = 'YES'
time = 0
while time < 3:
    not_up_arr = []

    for i in range(1, N+1):
        if arr[i] > arr[i+1]:
            not_up_arr.append(i)
            result.append(i)
            cnt -= 1
        if i == N and arr[i] < arr[i-1]:
                not_up_arr.append(i)
                result.append(i)
                cnt -= 1
    if cnt < 0:
        able = 'NO'
    while not_up_arr:
        tmp = not_up_arr.pop()
        arr[tmp] = arr[tmp+1]
    
    time += 1

if able == "YES":
    result.sort()
    print(able)
    print(len(result))
    for i in result:
        print(i, arr[i])
else:
    print(able)