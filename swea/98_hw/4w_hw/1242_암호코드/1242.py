import sys
sys.stdin = open('1242.txt')

pw_dict = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    code = [''.join(map(lambda x: f'{int(x, base=16):04b}', input().strip())) for _ in range(N)]

    print(f'#{tc}', end=' ')
    # 정답 저장할 변수
    result = 0

    # 코드 순회
    for x in range(N):
        if '1' in code[x]:
            y = 0
            tmp = []

            while y != M * 4:
                if (x == 0 and code[x][y] == '1') or (code[x][y] == '1' and code[x - 1][y] == '0'):
                    c = {0: 0, 1: 0, 2: 0, 3: 0}

                    for k in range(4):
                        while code[x][y] == str(k % 2):
                            c[k] += 1
                            y += 1

                    p_key = min(c[1], c[2], c[3])

                    tmp.append(pw_dict[(c[1] // p_key, c[2] // p_key, c[3] // p_key)])

                    ans = 0

                    if len(tmp) == 8:
                        for i in range(8):
                            if i % 2:
                                ans += tmp[i]
                            else:
                                ans += tmp[i] * 3

                        if ans % 10:
                            pass
                        else:
                            result += sum(tmp)

                        tmp = []
                y += 1
    print(result)