# N = int(input())

# tan = list(map(int, input().split()))
# tan.append(0)
# tang = []
# i = 0
# while i < N:
#     tmp = tan[i]
#     tmpl = [tmp]
#     for j in range(i+1, N+1):
#         if tmp != tan[j]:
#             break
#         else:
#             tmpl.append(tan[j])
#     i = j
#     tang.append(tmpl)

# tmp = 0
# cnt = 0
# if len(tang) == 1:
#     cnt = len(tang[0])
# else:
#     for i in range(len(tang)-1):
#         if i < len(tang)-2 and tang[i][0] == tang[i+2][0]:
#             tmp = len(tang[i]) + len(tang[i+1]) + len(tang[i+2])
#         else:
#             tmp = len(tang[i]) + len(tang[i+1])
#         cnt = max(tmp, cnt)

# print(cnt)

# def max_length_with_two_fruits(N, fruits):
#     max_length = 0
    
#     for a in range(N):
#         for b in range(N):
#             if a + b >= N:
#                 break

#             used_fruits = set(fruits[a:N-b])  # 앞쪽에서 a개, 뒤쪽에서 b개의 과일을 사용
#             if len(used_fruits) <= 2:
#                 max_length = max(max_length, N - a - b)

#     return max_length

# # 입력 예시
# N = 10
# fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

# # 결과 출력
# result = max_length_with_two_fruits(N, fruits)
# print(result)


def max_length_with_two_fruits(N, fruits):
    max_length = 0
    fruit_counts = {}

    left = 0
    for right in range(N):
        fruit = fruits[right]
        fruit_counts[fruit] = fruit_counts.get(fruit, 0) + 1

        while len(fruit_counts) > 2:
            left_fruit = fruits[left]
            fruit_counts[left_fruit] -= 1
            if fruit_counts[left_fruit] == 0:
                del fruit_counts[left_fruit]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

N = int(input())
fruits = list(map(int, input().split()))

max_len = 0
cnt = {}

left = 0
for right in range(N):
    fruit = fruits[right]
    cnt[fruit] = cnt.get(fruit, 0) + 1

    while len(cnt) > 2:
        left_fr = fruits[left]
        cnt[left_fr] -= 1
        if cnt[left_fr] ==0:
            del cnt[left_fr]
        left += 1
    max_len = max(max_len, right-left + 1)

print(max_len)