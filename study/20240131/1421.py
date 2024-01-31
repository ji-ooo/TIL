N, C, W = map(int, input().split())

trees = []
for _ in range(N):
    trees.append(int(input()))
trees.sort()

result = 0
while trees:
    length = trees[-1]
    while length > 0:
        cut = 0
        cnt = 0
        for tree in trees:
            if tree//length * C < tree//length * W:
                if tree%length != 0:
                    cut += tree//length
                else:
                    cut += tree//length -1
                cnt += tree//length
            else:
                if tree == length:
                    cnt += 1
        
        money = W * length * cnt - C * cut
        result = max(result, money)
        length -= 1

    trees = trees[1:]
print(result)