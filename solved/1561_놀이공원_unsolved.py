import sys
input = sys.stdin.readline

N, M = map(int, input().split())
need_time = list(map(int, input().split()))
time = {}

for i in need_time:
    time[i] = 1

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

if M >= 2:
    i = 2
    l = lcm(need_time[0], need_time[1])
    while i < M:
        l = lcm(l, need_time[i])
        i += 1
l = int(l)

cycle = M
for i in range(1, l):
    for j in need_time:
        if i%j == 0:
            cycle += 1

if N >= cycle:
    N %= cycle

ans = 0
if N <= M:
    ans = N
else:
    for i in range(1, l):
        for j in range(M):
            k = need_time[j]
            
            if i%k == 0 and N > 0:
                N -= 1
            
                if N == 0:
                    ans = j
                    if ans == 0:
                        ans = need_time[-1]
                    break
        if ans != 0:
            break

print(ans)


'''
0  12345
1  1
2  12
3  1 3
4  12 4
5  1   5
6  123
7  1
8  12 4
9  1 3
10 12  5
11 1
12 1234
13 1
14 12   
15 1 3 5
16 12 4
17 1
18 123
19 1  
20 12 45
최소공배수 마다 1사이클
n의 약수 전부 운행 가능
최소공배수로 나누고 나머지 + 계산 ?

0 32
1 -
2 -2
3 3
4 -2
5 -
6 32
'''