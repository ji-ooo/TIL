T = int(input())

for tc in range(1, T+1):
    card_lst = list(map(int, input()))

    card_cnt = {i: 0 for i in range(0, 12)}

    for card in card_lst:
        card_cnt[card] += 1

    tri, r = 0, 0

    for num in range(0, 10):
        while card_cnt[num] >= 3:
            card_cnt[num] -= 3
            tri += 1
        while card_cnt[num] >= 1 and card_cnt[num+1] >= 1 and card_cnt[num+2] >= 1:
            for i in range(3):
                card_cnt[num+i] -= 1
            r += 1

    if tri+r == 2: print(f'#{tc} true')
    else: print(f'#{tc} false')


