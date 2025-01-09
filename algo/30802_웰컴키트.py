N = int(input())

sizes = list(map(int, input().split()))
t, p = map(int, input().split())

ans = 0

for i in range(len(sizes)):
    ans += sizes[i]//t + (1 if sizes[i]%t else 0)

print(ans)
print(N//p, N%p)