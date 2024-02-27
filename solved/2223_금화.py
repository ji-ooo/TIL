t, x, m = map(int, input().split())

monsters = []
for i in range(m):
    monsters.append(list(map(int, input().split())))

ans = 0
faster = 1000001
D, S = 1000001, 1
for monster in monsters:
    d, s = monster
    
    hour = d//s + 1
    if d%s == 0: hour -= 1

    faster = min(faster, hour)

    if faster == hour:
        D, S = d, s

D_max_pos = D
while t > 0:
    if D - S > 0:
        D -= S
        ans += x
        
    elif D + S <= D_max_pos:
        D += S
        
    t -= 1

print(ans)