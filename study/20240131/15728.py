N, K = map(int, input().split())

share = list(map(int, input().split()))
team = list(map(int, input().split()))

mini_share = min(share)
maxi_share = max(share)

while len(team) > N-K:
    mini = maxi = 0

    tmp_mini = min(team)
    tmp_maxi = max(team)
    mini = tmp_mini * mini_share
    maxi = tmp_maxi * maxi_share

    if mini < maxi:
        team.remove(tmp_maxi)
    else:
        team.remove(tmp_mini)

mini = mini_share * min(team)
maxi = maxi_share * max(team)

if mini < maxi:
    print(maxi)
else: print(mini)

# for _ in range(K):
#     s = -100000000
#     r = 0
#     for i in team:
#         for j in share:
#             if s <= i*j:
#                 s = i*j
#                 r = i
    
#     team.remove(r)

# result = -100000000
# for t in team:
#     for s in share:
#         result = max(result, t*s)

# print(result)

