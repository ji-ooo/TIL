N = int(input())

coin_list = []
total = 0
for _ in range(N):
    won, cnt = map(int, input().split())
    total += won * cnt
    coin_list.extend([won]*cnt)

if total%2 == 1:
    result = 0

else:
    result = 0
    for i in range(1<<len(coin_list)):
        tmp = 0
        for j in range(len(coin_list)):
            if i & (1<<j):
                tmp += coin_list[j]
            if tmp > total//2:
                result = 0
                continue
            elif tmp == total//2:
                result = 1
                break
        if result:
            break
print(result)