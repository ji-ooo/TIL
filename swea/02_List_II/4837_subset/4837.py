import sys
sys.stdin = open('4837.txt')

T = int(input())

arr = [i for i in range(1, 13)]

for tc in range(1, T+1):
    N, K = map(int, input().split())

    cnt = 0
    # 1 ~ 12까지 집합, 비트 연산자 범위로 순회
    for i in range(1 << 12):
        # 임시 빈 배열
        lst = []

        # 12까지 순회, j의 비트를 i에 포함할 경우 lst에 부분집합 추가
        for j in range(12):
            if i & (1 << j):
                lst.append(arr[j])

        # 부분 집합의 합, 길이 검사 및 갯수 카운트
        if sum(lst) == K and len(lst) == N:
            cnt += 1

    print(f'#{tc} {cnt}')
