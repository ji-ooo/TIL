import sys
sys.stdin = open('4880.txt')


def winner(lst):
    length = len(lst)
    if length == 1:
        return lst
    elif length == 2:
        return lst
    else:
        left = lst[:length//2+1]
        right = lst[length//2+1:]
        winner(left)
        winner(right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_lst = list(map(int, input().split()))
    player_lst = [(card_lst, i+1) for i in range(N)]
    prev_win_lst = [(1, 3), (3, 2), (2, 1)]

    result = winner(player_lst)




    # print(f'#{tc} {player_lst[0]}')
