N, S, M = map(int, input().split())
v = list(map(int, input().split()))

arr = [[False] * (M+1) for _ in range(N+1)]
arr[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        if arr[i-1][j]:
            if j - v[i-1] >=0:
                arr[i][j - v[i-1]] = 1
            if j + v[i-1] <= M:
                arr[i][j + v[i-1]] = 1

for k in range(M, -1, -1):
    if arr[-1][k]:
        print(k)
        break
else:
    print(-1)

# 재귀하면 시간초과
# def volume(vol, i):
#     global result
#     print(vol, i)
#     if i == N:
#         result = max(result, vol)
#         return
    
#     if vol + tmp > M and vol - tmp < 0:
#         return
    
#     if result == M:
#         return
    
#     tmp = v[i]
#     if vol + tmp <= M:
#         volume(vol + tmp, i+1)
    
#     if vol - tmp >= 0:
#         volume(vol - tmp, i+1)

# result = -1
# volume(S, 0)
# print(result)