from itertools import permutations

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

result = set()
for i in permutations(num, M):
    result.add(i)

result = sorted(result)
for i in result:
    print(*i)