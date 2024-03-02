from itertools import combinations_with_replacement

N, M = map(int, input().split())
num = list(set(map(int, input().split())))
num.sort()
K = len(num)

for i in combinations_with_replacement(num, M):
    print(*i)

