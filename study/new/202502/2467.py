n = int(input())
sol = list(map(int, input().split()))           

start = 0
end = n - 1

x = y = 0
z = float('inf')

while start < end:
    mid = sol[start] + sol[end]

    if abs(mid) < z:
        x = sol[start]
        y = sol[end]
        z = abs(mid)

    if mid > 0:
        end -= 1
    elif mid < 0:
        start += 1
    else:
        break

print(x, y)