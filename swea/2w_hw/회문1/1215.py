import sys
sys.stdin = open('1215.txt')


# 회문인지 찾는 함수
def find(x, y):
    # 찾으려는 범위가 배열을 벗어나지 않도록 검사를 위한 변수
    nx, ny = x + N, y + N

    # 범위 안에 있을 때 N//2동안 반대쪽과 비교
    # 다르면 break, 멈추지 않았다면 갯수 + 1
    cnt = 0
    if nx <= 8:
        for i in range(N//2):
            if arr[x+i][y] != arr[x+N-1-i][y]:
                break
        else:
            cnt += 1

    if ny <= 8:
        for j in range(N//2):
            if arr[x][y+j] != arr[x][y+N-1-j]:
                break
        else:
            cnt += 1
    # 갯수 반환
    return cnt


for tc in range(1, 11):
    # N 및 배열 생성
    N = int(input())
    arr = []
    for _ in range(8):
        arr.append(list(map(str, input())))

    # 이차원 순회 하면서 결과에 갯수 더해줌
    result = 0
    for i in range(8):
        for j in range(8):
            result += find(i, j)
    print(f'#{tc} {result}')
