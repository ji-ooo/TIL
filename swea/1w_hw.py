import sys
sys.stdin = open('1w_hw.txt')
T = 10
for tc in range(1, T+1):
    N = int(input())
    line = list(map(int, input().split()))
    print(line)