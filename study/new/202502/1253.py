N = int(input())
nums = list(map(int, input().split()))
nums.sort()

ans = 0

for i in range(N):
    s = 0
    e = N - 1

    while s < e:
        if s == i:
            s += 1
            continue

        if e == i:
            e -= 1
            continue

        if nums[s] + nums[e] == nums[i]:
            ans += 1
            break

        elif nums[s] + nums[e] < nums[i]:
            s += 1

        else:
            e -= 1

print(ans)