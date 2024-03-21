import sys
sys.stdin = open('5653.txt')


def ex(cell):
    # 이번 한 단위 시간동안 세포가 생긴 좌표를 new_cell에 임시로 저장
    # 동시에 여러 세포가 활성화 되면 높은 수를 받아야 함
    new_cell = {}

    # 이번 한 단위 시간동안 죽은 세포의 좌표 잠깐 저장했다가, 마지막에 빼기
    now_dead = []

    # cell 순회하면서, point = key (세포 있는 좌표)
    for point in cell:
        # value 0번째 인자 = 현재 생명력
        # 현재 생명력이 0이면 활성화
        if cell[point][0] == 0:
            x, y = point
            # value 1번 인자 = 초기 생명력
            # 옆 칸에 넘겨줘야됨
            c = cell[point][1]

            # 주변 4칸에 세포 번식이 되는지 판단
            for dx, dy in ds:
                nx, ny = x + dx, y + dy
                np = (nx, ny)

                # 현재 세포가 없어야 함
                if np not in cell:
                    # 죽은 세포도 없어야되고
                    if np not in dead_cell:
                        # 이번에 세포가 새로 생긴 좌표라면
                        if np in new_cell:
                            # 더 높은 값 저장하게
                            new_cell[np] = max(new_cell[np], c)
                        # 아니면 그냥 저장
                        else:
                            new_cell[np] = c

        # 현재 생명력 하나 깎아줌
        # 마지막에 깎고, 다음 순회 때 0이면 활성화 되는 느낌
        cell[point][0] -= 1

        if cell[point][0] == -cell[point][1]:
            # 활성화 되고 X만큼 더 살았으면, -(초기생명력)
            # 이번에 죽은 세포 좌표 저장
            now_dead.append(point)


    # 이번에 세포 생긴 녀석들 좌표
    for new in new_cell:
        # cell 에 추가하기
        cell[new] = [new_cell[new], new_cell[new]]

    # 이번에 죽은 녀석들 좌표 dead
    for dead in now_dead:
        # cell 에서 빼고, dead_cell 저장
        cell.pop(dead)
        dead_cell.add(dead)


ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    # 살아있는 세포들 딕셔너리 cell 에 저장
    # key: 좌표, value: [현재 생명력, 초기 생명력]
    # 현재 생명력은 t마다 1씩 줄어들게, 초기 생명력은 활성화 시 넘겨줘야 함
    # 현재 생명력이 0이 되고 난 다음 턴에 활성화
    cell = {}
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(M):
            if line[j]:
                cell[(i, j)] = [line[j], line[j], 0]

    # 죽은 세포들 저장할 집합, 좌표만 저장
    dead_cell = set()
    act = set()
    # 시간 K동안 반복
    while K:
        ex(cell)
        K -= 1

    print(f'#{tc} {len(cell)}')
