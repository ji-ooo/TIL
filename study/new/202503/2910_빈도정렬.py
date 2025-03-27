N, C = map(int, input().split())
arr = list(map(int, input().split()))

num = {}
ans = []

for i in arr:
    if i not in num:
        num[i] = 1
    else:
        num[i] += 1

nums = list(num.items())
nums.sort(key=lambda x: -x[1])

for x, y in nums:
    ans.extend([x] * y)

print(*ans)
