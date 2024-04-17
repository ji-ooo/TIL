import sys
input = sys.stdin.readline

N = int(input())

ele = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    a, b = ele[i]
    for j in range(N):
        pass

'''
전깃줄이 안 겹치게 하기위해 몇 개 없애야 함
최소로 없애는 개수

겹치는 조건
    시작점이 더 큰 숫자 => 끝점 더 작은 숫자
    시작점이 더 작은 숫자 => 끝점 더 큰 숫자
    
안겹치는거 세는게 더 나을듯
'''
