card_lst = list(map(int, input()))

card_cnt = {i: 0 for i in range(0, 12)}

for card in card_lst:
    card_cnt[card] += 1

tri, run = 0, 0

for num in range(0, 10):
    while card_cnt[num] >= 3:
        card_cnt[num] -= 3
        tri += 1
    while card_cnt[num] == 1 and card_cnt[num+1] == 1 and card_cnt[num+2] == 1:
        for i in range(3):
            card_cnt[num+1] -= 1
        run += 1

if tri+run == 2: print('Baby-gin')
else: print('lose')


