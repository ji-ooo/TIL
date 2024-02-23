import sys
sys.stdin = open('1242.txt')

pw_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
           '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = []
    for _ in range(N):
        line = input().strip('0')

        if not line:
            continue

        # 중복된 코드 검사 여러 번 하지 않도록
        if code and line in code:
            continue
        else:
            code.append(line)

    code.sort(key=lambda x: len(x))
    for cd in range(len(code)-1):
        for i in range(cd+1, len(code)):
            code[i] = code[i].replace(code[cd], '').strip('0')

    # 정답 저장할 변수
    result = 0

    # 코드 순회
    for cd in code:
        # 16진수 => 2진수 변경, 오른쪽 0 제거
        cd = format(int(cd, 16), 'b').rstrip('0')

        # 길이가 56의 배수가 되도록 앞에 0 추가
        if len(cd)%56 != 0:
            z = 56 - len(cd)%56
            cd = '0' * z + cd

        # 56, 112, ... 일 때 몇 배수인지 확인
        times = len(cd) // 56

        # 코드를 체크하기 위해 리스트에 저장
        ch_cd = []

        # 56의 배수일 경우, 암호코드의 비율만 확인하면 되므로, times씩 건너뛰면서 저장
        for c in range(0, len(cd), times):
            ch_cd.append(cd[c])
        # 올바른 암호인지 체크할 변수
        check = 0

        # 암호화 된 코드 검증 숫자 저장할 리스트
        pw = []
        tmp = 0

        # 2진수 코드를 왼쪽부터 7개씩 c에 저장 => pw 리스트에 저장
        for i in range(0, 56, 7):
            c = ''
            for j in range(7):
               c += ch_cd[i+j]
            pw.append(pw_dict[c])

        # pw 순회하면서 올바른 암호코드인지 확인
        for num in range(8):
            if num%2 == 1:
                check += pw[num]
            else:
                check += pw[num] * 3
            tmp += pw[num]

        if check % 10 == 0:
            result += tmp
    print(f'#{tc} {result}')


    '''
    dec = ['0001101', '0011001', '0010011', '0111101', '0100011',
       '0110001', '0101111', '0111011', '0110111', '0001011']
 
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    answer_sum = 0
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] != '0' and visited[i][j] == 0:
                password_0b = bin(int(arr[i][j], 16))[2:].zfill(4)
                last_x, last_y = i, j
                find_ratio = False
                find_zero_cnt = False
                ratio = 0
                while not find_ratio:
                    ratio += 1
                    password_0b = '0' * (8-len(bin(int(arr[last_x][last_y-2:last_y], 16))[2:].zfill(4))) + bin(int(arr[last_x][last_y-2:last_y], 16))[2:].zfill(4) + password_0b
                    if not find_zero_cnt:
                        find_zero_cnt = True
                        zero_cnt = 0
                        while password_0b[-(zero_cnt+1)] == '0':
                            zero_cnt += 1
                    end = -(zero_cnt+1)
                    change_num_cnt = 0
                    for k in range(7*ratio):
                        if password_0b[end-k] != password_0b[end-k-1]:
                            change_num_cnt +=1
                    if change_num_cnt >= 4:
                        find_ratio = True
                        if end == -1:
                            real_pwd = bin(int(arr[i][j-14*ratio:j+1], 16))[2:].zfill(4)
                        else:
                            real_pwd = bin(int(arr[i][j-14*ratio:j+1], 16))[2:].zfill(4)[:end+1]
                        real_pwd = '0' * ((56*ratio)-len(real_pwd)) + real_pwd
                        if len(real_pwd) == 56*ratio + 4:
                            real_pwd = real_pwd[4:]
                    else:
                        last_y -= 2
                while arr[last_x][j] != '0':
                    change_arr = [1] * (14 * ratio + 1)
                    visited[last_x][j-14*ratio:j+1] = change_arr
                    last_x += 1
                pwd, sum = 0, 0
                for k in range(8):
                    if k % 2 == 0:
                        pwd += dec.index(real_pwd[7*k*ratio : 7*(k+1)*ratio : ratio]) * 3
                    else:
                        pwd += dec.index(real_pwd[7*k*ratio : 7*(k+1)*ratio : ratio])
                    sum += dec.index(real_pwd[7*k*ratio : 7*(k+1)*ratio : ratio])
                if pwd % 10 == 0:
                    answer_sum += sum
    print(f'#{tc} {answer_sum}')
    
    '''