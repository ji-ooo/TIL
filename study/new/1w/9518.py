dr = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]

r, s = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(input()))

ans = 0
cnt = 0

for i in range(r):
    for j in range(s):
        tmp = 0
        for di, dj in dr:
            if 0 <= i + di < r and 0 <= j + dj < s:
                if arr[i+di][j+dj] == 'o':
                    tmp += 1

        if arr[i][j] == '.':
            if tmp > cnt:
                cnt = tmp
        else:
            ans += tmp
    
ans //= 2
ans += cnt

print(ans)
# for i in range(r):
#     for j in range(s):
#         if arr[i][j] == 'o':
#             continue

#         tmp = 0

#         for di, dj in dr:
#             if 0 <= i + di < r and 0 <= j + dj < s:
#                 if arr[i+di][j+dj] == 'o':
#                     tmp += 1
        
#         if tmp > res:
#             res = tmp

# ans += res
