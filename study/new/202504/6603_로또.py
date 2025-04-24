import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    line = input().strip()
    n, *nums = list(map(int, line.split()))

    if n == 0:
        exit()

    combs = list(combinations(nums, 6))
    for comb in combs:
        print(" ".join(map(str, comb)))
    print()
