N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]

result = []

s2 = []
s1 = []
s0 = []

for n, s, b in num:
    if s == 3:
        print(1)
        break
    elif s == 2:
        s2.append(n)
    elif s == 1:
        s1.append((n, b))
    else:
        s0.append((n, b))

able = []
if len(s2) > 1:
    a = str(s2[0])
    b = str(s2[1])
    if a[0] == b[0] and a[1] == b[1]:
        for i in range(1, 10):
            if i != a[2]:
                able.append(str(a[0]) + str(a[1]) + str(i))
    elif a[1] == b[1] and a[2] == b[2]:
        for i in range(1, 10):
            if i != a[0]:
                able.append(str(a[0]) + str(a[1]) + str(i))
    else:
        for i in range(1, 10):
            if i != a[1]:
                able.append(str(a[0]) + str(i) + str(a[2]))
else:
    a = str(s2[0])
    for i in range(1, 10):
            if i != a[2]:
                able.append(str(a[0]) + str(a[1]) + str(i))
    for i in range(1, 10):
            if i != a[0]:
                able.append(str(a[0]) + str(a[1]) + str(i))
    for i in range(1, 10):
            if i != a[1]:
                able.append(str(a[0]) + str(i) + str(a[2]))
print(able)

# for x in s1:



'''
생각하고 있을 가능성이 있는 답 ?
은 생각 할 수 없는 거 다 빼라는 뜻

3 st
2s
1s 2b
1s 1b
1s 0b
0s 3b
0s 2b
0s 1b
0s 0b

'''