import sys
sys.stdin = open('Ladder.txt')

for _ in range(10):
    tc = int(input())

    # 2차원 배열
    arr = []
    for i in range(100):
        line = list(map(int, input().split()))
        arr.append(line)

    # 막대 위치 기록, 1이거나 2이면 추가 + 2일때 위치 저장
    rod_list = []
    for rod in range(100):
        if line[rod] == 1:
            rod_list.append(rod)
        if line[rod] == 2:
            rod_list.append(rod)
            pos = len(rod_list)-1

    # 현재 위치
    row = 99
    col = rod_list[pos]

    # 옆이 1이면 다음 막대 위치까지 이동
    for _ in range(100):
        if col > 0 and arr[row][col-1] == 1:
            pos -= 1
            col = rod_list[pos]
        elif col < 99 and arr[row][col+1] == 1:
            pos += 1
            col = rod_list[pos]
        row -= 1

    print(f'#{tc} {col}')
