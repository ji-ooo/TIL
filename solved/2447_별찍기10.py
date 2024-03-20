'''
*을 다 칠해놓고
재귀로 쭉 들어가면서 없애기
'''

def d_star(n, r, c):
    for i in range(n//3, n*2//3):
        for j in range(n//3, n*2//3):
            star[r+i][c+j] = ' '
    if n > 3:
        for x in range(3):
            for y in range(3):
                if x == y == 1:
                    continue
                else:
                    d_star(n//3, r+x*(n//3), c+y*(n//3))


N = int(input())

star = [['*'] * N for _ in range(N)]

d_star(N, 0, 0)
for i in range(N):
    print(''.join(star[i]))
