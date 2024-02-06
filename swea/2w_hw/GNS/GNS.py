import sys
sys.stdin = open('GNS.txt')

T = int(input())
for tc in range(1, T+1):
    t, N = map(str, input().split())
    N = int(N)
    line = list(map(str, input().split()))
    # 0~9 까지 리스트에 등록
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # num 카운팅 할 빈 딕셔너리 생성
    numbers = dict()
    for i in num:
        numbers[i] = 0

    # input 에서 숫자 카운팅
    for n in line:
        numbers[n] += 1

    # 딕셔너리 키 * 밸류를 출력 할 결과 리스트에 추가
    result = []
    for x in num:
        tmp = [x] * numbers[x]
        result.extend(tmp)
    print(f'#{tc}')
    print(*result)