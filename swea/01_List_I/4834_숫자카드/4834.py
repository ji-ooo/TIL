import sys
sys.stdin = open('4834.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input()))
    cnt = {} # 카운팅 할 빈 딕셔너리 생성

    # 카드 카운팅 => 딕셔너리에 갯수 저장
    for c in card:
        cnt[c] = cnt.setdefault(c, 0) + 1

    # 딕셔너리 => 리스트, 정렬하기 위해
    card_cnt = list(cnt.items())
    # 카드 갯수를 기준으로 정렬
    card_cnt.sort(key=lambda x: x[1])

    # 마지막 카드 갯수 == max_cnt에 저장
    max_cnt = card_cnt[-1][1]

    # max_cnt와 갯수가 같은 카드 숫자 리스트
    max_card_lst = []
    for i in card_cnt:
        if i[1] == max_cnt:
            max_card_lst.append(i[0])
    max_card_lst.sort()
    print(f'#{tc} {max_card_lst[-1]} {max_cnt}')