import sys
sys.stdin = open('input.txt')

prime = [2, 3, 5, 7]
for i in range(10, 101):
    for j in range(2, 11):
        if i%j == 0:
            break
    else:
        prime.append(i)

for tc in range(1, int(input())+1):
    N = int(input())
    switch = list(map(int, input().split()))
    S = int(input())
    for g, c in list(map(int, input().split()) for _ in range(S)):
        if g == 1:
            for i in range(N):
                if i in prime:
                    now = i - 1
                    for change in range(-c, c+1):
                        x = now + change
                        if 0 <= x < N:
                            switch[x] += 1
        else:
            for d in range(1, c+1):
                if c%d == 0:
                    x = d - 1
                    switch[x] += 1

    print(f'#{tc}')
    switch = list(map(lambda x: x%2, switch))
    print(*switch)
