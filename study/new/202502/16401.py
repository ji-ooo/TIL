M, N = map(int, input().split())
arr = list(map(int, input().split()))

left = 1
right = 10**9
ans = 0

while left <= right:
    mid = (left + right) // 2
    tmp = 0

    for i in arr:
        tmp += i // mid

    if M <= tmp:
        if ans < mid:
            ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
