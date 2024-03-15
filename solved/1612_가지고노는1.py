N = int(input())

num = 2
if N%2 == 0 or N%5 == 0:
    print(-1)
elif N == 1:
    print(1)
else:
    i = 11
    while i%N:
        i %= N
        i *= 10
        i += 1
        num += 1
    print(num)

# nums = []
# for i in range(1, int(num**(1/2))):
#     if num%i == 0:
#         nums.append((i, num//i))
# print(nums)
