import sys
sys.stdin = open('4836.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 색칠하는 범위, 색 리스트에 저장
    color = []
    for _ in range(N):
        color.append(list(map(int, input().split())))

    # 2차원 배열 생성
    arr = []
    line = [0] * 10
    for _ in range(10):
        arr.append(line[:])

    cnt = 0

    # 색칠 리스트 순회
    for i in color:
        # 색이 1일 때
        # 인덱스 값이 이미 2일때 보라색 갯수 + 1 / 아닐 때 인덱스 값 = 1
        if i[4] == 1:
            for x in range(i[0], i[2]+1):
                for y in range(i[1], i[3]+1):
                    if arr[x][y] == 2:
                        cnt += 1
                    else:
                        arr[x][y] = 1
        # 색이 2일 때 반대로 똑같이 진행
        else:
            for x in range(i[0], i[2]+1):
                for y in range(i[1], i[3]+1):
                    if arr[x][y] == 1:
                        cnt += 1
                    else:
                        arr[x][y] = 2

    print(f'#{tc} {cnt}')
