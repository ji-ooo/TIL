import sys
sys.stdin = open('5644.txt')

dr = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
for tc in range(1, int(input())+1):
    M, A = map(int, input().split())
    ma = list(map(int, input().split()))
    mb = list(map(int, input().split()))
    BC = []
    for _ in range(A):
        x, y, c, p = map(int, input().split())
        x -= 1
        y -= 1
        BC.append([x, y, c, p])
    # x, y, c, p: (좌표), 범위, 용량

    able = {}
    for n, bc in enumerate(BC):
        x, y, c, p = bc
        for i in range(y-c, y+c+1):
            for j in range(x-c, x+c+1):
                if 0 <= i < 10 and 0 <= j < 10:
                    if abs(y-i) + abs(x-j) <= c:
                        if (i, j) in able:
                            able[(i, j)].append((n, p))
                            able[(i, j)].sort(key=lambda x:-x[1])
                        else:
                            able[(i, j)] = [(n, p)]
    result = [0, 0]
    a = (0, 0)
    b = (9, 9)
    t = 0
    while t <= M:
        if a in able and b in able:
            if able[a][0][0] == able[b][0][0]:
                if len(able[a]) > 1 and len(able[b]) > 1:
                    if able[a][1][1] >= able[b][1][1]:
                        result[0] += able[a][1][1]
                        result[1] += able[b][0][1]
                    else:
                        result[0] += able[a][0][1]
                        result[1] += able[b][1][1]
                elif len(able[a]) > 1:
                    result[0] += able[a][1][1]
                    result[1] += able[b][0][1]
                elif len(able[b]) > 1:
                    result[0] += able[a][0][1]
                    result[1] += able[b][1][1]
                else:
                    result[0] += able[a][0][1] // 2
                    result[1] += able[b][0][1] // 2
            else:
                result[0] += able[a][0][1]
                result[1] += able[b][0][1]

        elif a in able:
            result[0] += able[a][0][1]

        elif b in able:
            result[1] += able[b][0][1]


        if t == M:
            break
        da = dr[ma[t]]
        db = dr[mb[t]]
        a = (a[0] + da[0], a[1] + da[1])
        b = (b[0] + db[0], b[1] + db[1])
        t += 1

    print(f'#{tc} {sum(result)}')
    '''
    충전 가능한 좌표를 딕셔너리에 담기
    (0, 0): [(1, 100), (2, 70)]
    key에 좌표 value에 bc
    bc는 리스트로 bc 기기 번호, 충전 용랼
    t초 일 때, A와 B가 같은 기기 번호를 받으면
    다른 번호가 가능한 사람은 옮길 수 있게
    안되면 반으로 나누기
    기기 번호보다 출력 용량이 중요한듯 그럼
    '''