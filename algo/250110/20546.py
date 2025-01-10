j = s = int(input())
J = S = 0

arr = list(map(int, input().split()))

for i in range(len(arr)):
    if j >= arr[i]:
        J += j//arr[i]
        j %= arr[i]

    if i < 3:
        continue
    if arr[i] < arr[i-1] < arr[i-2] < arr[i-3]:
        if s >= arr[i]:
            S += s//arr[i]
            s %= arr[i]
    elif arr[i] > arr[i-1] > arr[i-2] > arr[i-3]:
        if S:
            s += S*arr[i]
            S = 0

a = J*arr[-1]+j
b = S*arr[-1]+s

if a == b:
    print("SAMESAME")
elif a > b:
    print("BNP")
else:
    print("TIMING")
