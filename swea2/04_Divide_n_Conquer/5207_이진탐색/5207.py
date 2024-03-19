import sys
sys.stdin = open('5207.txt')


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 이진탐색을 위해 A 정렬
    A.sort()

    # 정답 갯수
    cnt = 0

    # B 값 순회
    for i in B:

        # 왼쪽 갔는지 오른쪽 갔는지 체크하는 변수
        case = 0
        if A[0] <= i <= A[-1]:
            # 이진탐색
            s = 0
            e = N-1
            while s <= e:
                mid = (s+e)//2
                if A[mid] > i:
                    # 왼쪽으로 가면 case == 1
                    # case가 1일 때 또 왼쪽으로 왔으면 멈춤
                    if case == 1:
                        break
                    e = mid - 1
                    case = 1
                elif A[mid] < i:
                    # 오른쪽 case == 2
                    # 오른쪽일 때 case=2면 멈춤
                    if case == 2:
                        break
                    s = mid + 1
                    case = 2
                # 위에 다 지나왔으면 갯수 +1
                else:
                    cnt += 1
                    break
    print(f'#{tc} {cnt}')