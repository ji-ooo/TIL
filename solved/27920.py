N = int(input())

# if N%2 == 1:
#     l_list = [i for i in range(N-2, 0, -2)]
#     r_list = [i for i in range(N%2+1, N, 2)]
#     center = [N]
#     card = l_list + center + r_list
#     t = []
#     i = 0
#     while len(t) != N-1:
#         t.append(N-i)
#         t.append(i+1)
#         i +=1
#     t.append((N+1)//2)

# else:
#     l_list = [i for i in range(N-2, 0, -2)]
#     r_list = [i for i in range(N%2+1, N, 2)]
#     center = [N]
#     card = l_list + center + r_list
#     t = []
#     i = 0
#     while len(t) != N:
#         t.append(N-i)
#         t.append(i+1)
#         i +=1

l_list = [i for i in range(N-2, 0, -2)]
r_list = [i for i in range(N%2+1, N, 2)]
center = [N]
card = l_list + center + r_list
t = []
i = 0
while len(t) != N-N%2:
    t.append(N-i)
    t.append(i+1)
    i +=1
if N%2 == 1:
    t.append((N+1)//2)

print('YES')
print(*card)
print(*t)

