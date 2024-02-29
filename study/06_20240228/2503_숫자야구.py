N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]

base_lst = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue
            else:
                base_lst.append([i, j, k])

i = 0
while i != len(base_lst):
    now_n = base_lst[i]
    r = False

    for comp_n in num:
        t = list(map(int, str(comp_n[0])))
        S, B = comp_n[1], comp_n[2]
        s = b = 0
        for x in range(3):
            if now_n[x] == t[x]:
                s += 1
            elif now_n[x] in t:
                b += 1

        if s != S or b != B:
            r = True
            base_lst.remove(now_n)
            break

    if r: continue
    else: i += 1

print(len(base_lst))