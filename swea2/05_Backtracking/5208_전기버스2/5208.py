import sys
sys.stdin = open('5208.txt')


def move(cur, battery, count):
    global result
    # 현재 위치에서 남은 배터리(이동 최대 거리)를 더해보고
    # 목표지점보다 멀리 갈 수 있으면 최소값 비교 및 return
    if cur + battery >= N-1:
        result = min(count, result)
        return

    # 최소 횟수를 찾는 문제이므로,
    # 현재 교체 횟수가 지금까지 최소 횟수보다 많거나 같으면 그만 봐도 된다
    if count >= result:
        return

    # 다음 정류장부터, 최대 이동 가능 정류장 까지 다 가봄
    for i in range(1, battery+1):
        move(cur + i, arr[cur + i], count + 1)


for tc in range(1, int(input())+1):
    N, *arr = list(map(int, input().split()))
    result = N

    bat = arr[0]
    cnt = 0

    # 현재 위치, 현재 배터리, 교환 횟수
    move(0, bat, cnt)
    print(f'#{tc} {result}')