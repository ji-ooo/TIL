import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
'''
백트래킹 해야될듯
tetri1 = [(0, 1), (0, 1), (0, 1)]
tetri2 = [(0, 1), (1, 0), (1, 1)]
tetri3 = [밑 밑 오]
tetri4 = [밑 오 오]
이런 느낌으로 ?

'''