import sys
sys.stdin = open('1240.txt')
from collections import deque


pw_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
           '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = []
    for _ in range(N):
        line = int(input())
        line = str(line)
        line = list(map(int, line))
        for i in range(len(line)-1, -1, -1):
            if line[i] == 1:
                break
        else:
            continue
        line = line[:i+1]
        while len(line)%7 != 0:
            line = [0]+line

        if code and code[0] == line:
            continue
        else:
            code.append(line)

    t = deque(code[0])
    pw = []
    while t:
        c = ''
        for i in range(7):
            c += str(t.popleft())
        pw.append(pw_dict[c])

    check = 0
    result = 0
    for num in range(8):
        if num%2 == 1:
            check += pw[num]
        else:
            check += pw[num] * 3
        result += pw[num]

    if check % 10 != 0:
        result = 0

    print(f'#{tc} {result}')
