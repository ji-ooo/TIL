import sys
sys.stdin = open('2115.txt')


def findmx(x, y):
    global tmp

    t = 0
    for k in range(M):
        t += arr[x][y+k]


def honey(x, y, c, s):
    global result

    if c == 2:
        result = max(result, s)
        return

    else:
        for k in range(M):


            s += arr[x][y+k]**2

        for i in range(x, N):
            if i == x:
                for j in range(y+M, N-M+1):
                    honey(i, j, c + 1, s)

            else:
                for j in range(N-M+1):
                    honey(i, j, c + 1, s)


for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N-M+1):
            tmp = 0
            findmx(i, j)
            # C에 가장 가깝게 채취할 수 있는 통
            # 한 번에 추출하는게 제일 이득임
            # 7,2 보다 9 하나 뽑는게 더 낫다
            # 함수 하나 더 해서? 최대가 되는 인덱스 리스트를 리턴
            # 수익이 제곱으로 나서 큰 수 위주로 채취
            # 최대값으로 다 바꿔놓고 다시 돌리기?

            for k in range(M):
                honey(i, j, 0, 0)

    print(result)