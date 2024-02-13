import sys
sys.stdin = open('4408.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [0 for _ in range(201)]
    for _ in range(N):
        s, e = map(int, input().split())
        S, E = (s+1)//2, (e+1)//2
        if S < E:
            while S <= E:
                room[S] += 1
                S += 1
        else:
            while S >= E:
                room[S] += 1
                S -= 1

    print(f'#{tc} {max(room)}')




'''
짝수든 홀수든 복도 막는거는 똑같음
N//2 씩 리스트 두개 => 인덱스 2개씩 묶어서 하나 리스트로 해도 될듯
시작 인덱스 ~ 끝 인덱스 사이 범위에 겹치면 같이 못감

'''