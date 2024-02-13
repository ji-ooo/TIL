import sys
sys.stdin = open('1219.txt')

from collections import deque

for tc in range(1, 11):
    T, N = map(int, input().split())
    line = deque(list(map(int, input().split())))

    # 길 연결을 딕셔너리로 저장
    # 노드가 99까지 있으므로 100까지 미리 생성
    road = {i:[] for i in range(100)}

    # 입력 받은 순서대로 2개씩 pop, 출발점 => 도착점 딕셔너리에 저장
    for _ in range(N):
        x, y = line.popleft(), line.popleft()
        road[x].append(y)

    # 방문한 노드 저장할 리스트, 다음 탐색할 노드 que에 저장
    visited = [False] * 100
    que = deque([0])

    # 탐색 전 도착 못한다고 가정
    result = 0
    # que가 있는 동안 반복
    while que:
        # 현재 탐색할 지점 v, 방문 노드 저장
        v = que.pop()
        visited.append(v)

        # 현재 노드를 key로 순회하며 도착 노드를 방문한 적이 없다면 que에 저장
        for i in road[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
            # 다음 탐색할 지점이 99라면, 길이 있다는 뜻 => result = 1
            if i == 99:
                result = 1

        # 99에 도착할 수 있다면 더 이상 탐색할 필요 없음
        if 99 in que:
            break

    print(f'#{tc} {result}')
