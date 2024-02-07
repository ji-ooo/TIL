import sys
sys.stdin = open('4880.txt')


def winner(lst):
    length = len(lst)
    i = 0
    j = length-1
    if length == 1:
        return lst[0]
    elif length == 2:
        prev = lst[0][0]
        nxt = lst[1][0]
        if (prev, nxt) in win_lst:
            return lst[0]
        else:
            return lst[1]
    else:
        left = lst[:(j-i)//2+1]
        right = lst[(j-i)//2+1:]
        return winner([winner(left), winner(right)])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_lst = list(map(int, input().split()))
    player_lst = [(card_lst[i], i+1) for i in range(N)]
    win_lst = [(1, 3), (3, 2), (2, 1), (1, 1), (2, 2), (3, 3)]

    result = winner(player_lst)[1]

    print(f'#{tc} {result}')
