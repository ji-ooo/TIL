from itertools import combinations

def make_team(home, home_stat, away_stat):
    global result
    tmp = []
    ttmp = []
    for n in range(N):
        if n in home:
            for i in tmp:
                home_stat += arr[i][n] + arr[n][i]
            tmp.append(n)
        else:
            for i in ttmp:
                away_stat += arr[i][n] + arr[n][i]
            ttmp.append(n)
    result = min(abs(home_stat - away_stat), result)
    
    
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 100*20

comb = list(combinations(range(N), N//2))
home_team = comb[:len(comb)//2]
for h in home_team:
    make_team(h, 0, 0)
print(result)


'''
N C (N//2)
'''

# def leaves_team(num, stat):
#     away_team = []
#     away_stat = 0
#     for n in range(N):
#         if n not in num:
#             for i in away_team:
#                 away_stat += arr[i][n] + arr[n][i]
#             away_team.append(n)
#     print(away_team, num, away_stat)
#     return abs(away_stat - stat)