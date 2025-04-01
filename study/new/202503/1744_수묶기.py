import sys
input = sys.stdin.readline

N = int(input())
pos = []
neg = []
z = 0

for _ in range(N):
    n = int(input())
    if n > 0:
        pos.append(n)
    elif n < 0:
        neg.append(n)
    else:
        z += 1

pos.sort()
neg.sort(reverse=True)

ans = 0

while len(pos) >= 2:
    a, b = pos.pop(), pos.pop()
    if b != 1:
        ans += a * b
    else:
        ans += a + b

while len(neg) >= 2:
    a, b = neg.pop(), neg.pop()
    ans += a * b

if neg and z:
    z -= 1
    neg.pop()

if pos:
    ans += pos.pop()
if neg:
    ans += neg.pop()

print(ans)