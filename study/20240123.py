import itertools

n = int(input())
lst = []
cur = 0
while n != 0:
    while len(lst) <= n:
        Cur = str(cur)
        tmp = set()
        for i in Cur:
            tmp.add(int(i))
            if len(tmp) == len(Cur):
                lst.append(cur)
        cur += 1

    print(lst[n])
    n = int(input())

'''
11 99
100
101
11x
1x1
200

x%11 == 0 
x//11 == 10 * y
x%100 == 0
'''

'''
str(n)
tmp = {}
for i in n:
    tmp.append(i)

'''