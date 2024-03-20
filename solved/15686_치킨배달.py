import sys
input = sys.stdin.readline

'''
c1) 2 마다 bfs
or
c2) 1 마다 bfs

c1이면, 모든 집 까지 거리 탐색?
다른 치킨집과 거리 비교하기가 애매해 지는 거 같다

c2이면, 가장 가까운 치킨집 까지 거리는 ok
얘도 거리 비교가 애매한듯
모든 치킨집 까지 거리 체크해서 치킨집 위치에 거리를 저장?

c1 이나 c2나 결국 치킨집에다가 집까지 거리 저장하는게 맞는거 같은데,.

그리디하게 모든 집까지 거리가 가장 작은 치킨집을 선택해도 되는가
안됨 확실하게

치킨집 선택이 다 되고 나야 거리 비교가 제대로 가능한데

치킨 집을 선택하는 기준이 우선되어야 함 => 다음 거리 계산
근데 치킨 집을 선택하는 기준이 거리임

다 선택해보고 백트래킹? 개오래걸릴듯
백트래킹 말고 가능한게 있나
얘가 제일 현실적인듯
'''

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

backtrack(0, 0) # 치킨 집 개수, 거리