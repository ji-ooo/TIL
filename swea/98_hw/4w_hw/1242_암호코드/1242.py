import sys
sys.stdin = open('1242.txt')
from collections import deque

pw_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
           '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = []
    # 0을 기준으로 분리해서 코드 찾음
    for _ in range(N):
        line = input().strip()
        if line.isdigit():
            if int(line) == 0:
                continue

        line = list(line.split('0'))
        # 중복된 코드 검사 여러 번 하지 않도록
        for i in line:
            if i != '':
                if code and i in code:
                    continue
                else:
                    code.append(i)

    # 정답 저장할 변수
    result = 0

    # 코드 순회
    for cd in code:
        # 16진수 => 2진수 변경
        cd = str(format(int(cd, 16), 'b'))

        # 끝에 0이 포함된 경우는 없기 때문에 0 다 잘라줌
        for i in range(len(cd) - 1, -1, -1):
            if cd[i] == '0':
                continue
            else:
                break
        cd = cd[:i+1]

        # 0을 기준으로 분리했기 때문에, 16진수 내에 0이 있는 경우도 생각해야 함

        # 2진수로 전환할 때 길이가 52보다 작을 경우,
        # 0000으로 시작하는 암호 코드는 없으므로 16진수 코드를 받는 과정에서
        # 0이 포함되어 있는 코드가 분리되었다고 생각 => 0을 사이에 넣고 다음 인덱스에 저장
        # 이후 다음 코드부터 for 문 다시 진행
        if len(cd) <= 52:
            code[1] = code[0] + '0' + code[1]
            continue

        # 위 조건을 다 통과했다면, 길이가 56의 배수가 되도록 앞에 0 추가
        if len(cd)%56 != 0:
            z = 56 - len(cd)%56
            cd = '0' * z + cd

        # 56, 112, ... 일 때 다른 조건으로 진행하기 위한 변수
        times = len(cd)//56

        # 올바른 암호인지 체크할 변수
        check = 0

        # 2진수로 변환된 코드를 덱에 저장
        # 이후 7단위씩 잘라서 popleft 할 예정이기 때문에
        t = deque(cd)

        # 암호화 된 코드 검증 숫자 저장할 리스트
        pw = []
        tmp = 0
        # 2진수 코드를 왼쪽부터 7단위씩 c에 더한 후 c가 올바른 암호코드인지 확인
        while t:
            c = ''

            # 56보다 큰 수 일 경우, pop 횟수를 times번 씩 해 주어야 함
            for i in range(7):
                for _ in range(times):
                    c += t.popleft()

            # 비율만 계산하면 되기 때문에, times씩 건너뛰면서 ch에 다시 저장
            ch = ''
            for x in range(0, len(c), times):
                ch += c[x]
            pw.append(pw_dict[ch])

        for num in range(8):
            if num%2 == 1:
                check += pw[num]
            else:
                check += pw[num] * 3
            tmp += pw[num]

        if check % 10 == 0:
            result += tmp
    print(f'#{tc} {result}')