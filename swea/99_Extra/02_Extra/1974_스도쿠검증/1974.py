import sys
sys.stdin = open('1974.txt')


def check_square(i, j):
    sq = []
    for x in range(3):
        for y in range(3):
           sq.append(arr[x+i][y+j])

    for i in range(1, 9):
        if sq[i] in sq[:i]:
            return 0
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    arr = []
    result = 1
    for _ in range(9):
        line = list(map(int, input().split()))

        for i in range(1, 9):
            if line[i] in line[:i]:
                result = 0
        arr.append(line)

    if result:
        for i in range(9):
            tmp = []
            for j in range(9):
                tmp.append(arr[j][i])

            for x in range(1, 9):
                if tmp[x] in tmp[:x]:
                    result = 0
                    break
            if not result:
                break

    if result:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                result = check_square(i, j)

                if not result:
                    break
            if not result:
                break

    print(f'#{tc} {result}')
