import sys
input = sys.stdin.readline

N, K = map(int, input().split())
char = []
for _ in range(N):
    char.append(int(input()))

start = 1
end = int(1e9)
while start <= end:
    mid = (start+end)//2
    tmp = 0
    cnt = 0
    # print(start, end, mid)
    for lv in char:
        if mid > lv:
            tmp += mid - lv
            cnt += 1
        elif mid == lv:
            cnt += 1
        # print(tmp, cnt)
    if tmp > K:
        end = mid-1
    elif tmp < K:
        if K - tmp < cnt:
            start = mid
            break
        start = mid + 1
    else:
        start = mid
        break
    # print(tmp)
    # print('----')
print(start)