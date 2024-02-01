N, C, W = map(int, input().split())

trees = []
for _ in range(N):
    trees.append(int(input()))

result = 0
length = 10000
while length > 0:
    cut = 0
    cnt = 0
    for tree in trees:
        if tree < length:
            continue

        tmp = tree//length
        tmp_cnt = tmp_cut = tmp

        if tree%length == 0:
            tmp_cut -= 1
        
        if tmp_cut*C < tmp_cnt*W*length:
            cnt += tmp_cnt
            cut += tmp_cut

    money = W * length * cnt - C * cut
    result = max(result, money)
    length -= 1

print(result)