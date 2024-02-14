import sys
sys.stdin = open('4880.txt')


# 이긴사람 찾을 함수
def winner(lst):
    length = len(lst)
    # 왼쪽, 오른쪽 인덱스
    i = 0
    j = length-1
    # 한명일 경우 바로 반환
    if length == 1:
        return lst[0]
    # 2명 일경우 가위바위보 진행, 이긴사람 반환
    elif length == 2:
        prev = lst[0][0]
        nxt = lst[1][0]
        if (prev, nxt) in win_lst:
            return lst[0]
        else:
            return lst[1]
    # 2명 이상일 경우 분할
    else:
        left = lst[:(j-i)//2+1]
        right = lst[(j-i)//2+1:]
        # 매개변수를 리스트 형태로 재귀
        return winner([winner(left), winner(right)])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_lst = list(map(int, input().split()))
    player_lst = [(card_lst[i], i+1) for i in range(N)]
    # 왼쪽 사람이 이기는 경우 리스트
    win_lst = [(1, 3), (3, 2), (2, 1), (1, 1), (2, 2), (3, 3)]

    # 이긴사람의 번호가 필요하므로
    result = winner(player_lst)[1]

    print(f'#{tc} {result}')
