# 2437 저울
_ = int(input())
weights = sorted(map(int, input().split()))

# 현재까지 측정 가능한 최대 무게
sum_v = 0

for w in weights:
    # 사이 간격이 1이 아니라면 종료
    if w > sum_v + 1:
        break
    sum_v += w

# 측정할 수 없는 가장 작은 무게 출력
print(sum_v + 1)

'''
문제의 요구사항 분석:
문제의 목표는 주어진 추들을 이용해 측정할 수 없는 가장 작은 무게를 찾는 것
즉, 가능한 가장 작은 값부터 측정할 수 없는 무게를 찾아야 함

문제의 특성 파악:
주어진 추들을 오름차순으로 정렬한 후,
작은 무게부터 시작해서 가능한 무게를 누적해 나가는 방식이 유효
무게는 같거나 차이가 1이하로 날때 측정가능
'''