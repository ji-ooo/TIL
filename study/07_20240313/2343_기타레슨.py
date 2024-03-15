import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
s = max(lst)
e = sum(lst)

while s <= e:
    num_sum = 0
    cnt= 1
    mid = (s+e)//2
    # print(mid)
    for i in lst:
        num_sum += i
        if num_sum > mid:
            cnt += 1
            num_sum = i
    
    if cnt > M:
        s = mid+1
    else:
        e = mid-1
if N == M :
    print(max(lst))
else:
    print(int(s))


# N, M = map(int, input().split())
# br = list(map(int, input().split()))
# start = max(br)
# end = int(1e9)
# result = 0
# while start <= end:
#     mid = (start+end)//2
#     cur = 0
#     cnt = 1
#     # print(start, end, mid)
#     for i in br:
#         if i < mid - cur:
#             cur += i

#         elif i == mid - cur:
#             cur = 0
#             cnt += 1

#         else:
#             cnt += 1
#             cur = i
#         # print(cur, cnt)
#     if cur == 0:
#         cnt -= 1

#     if cnt > M:
#         start = mid+1
    
#     elif cnt <= M:
#         end = mid-1
#         result = mid
#     # print('----')
# if not result:
#     result = max(br)
# print(result)