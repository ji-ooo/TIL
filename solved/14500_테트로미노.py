import sys
input = sys.stdin.readline

def tetro(v):
    x, y = v
    s = 0
    
    for directions in tetri:
        tmp = arr[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                tmp += arr[nx][ny]
            else:
                break
        s = max(s, tmp)
            
    return s


N, M = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
tetri = [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)], # 긴거
         [(0, 1), (1, 0), (1, 1)], # 네모
         [(1, 0), (2, 0), (2, 1)], [(1, 0), (2, 0), (2, -1)], [(0, 1), (0, 2), (1, 2)], [(0, 1), (0, 2), (-1, 2)], # L자
         [(1, 0), (1, 1), (1, 2)], [(1, 0), (1, -1), (1, -2)], [(0, 1), (1, 1), (2, 1)], [(0, 1), (-1, 1), (-2, 1)], # ㄴ자
         [(1, 0), (0, 1), (0, 2)], [(1, 0), (2, 0), (0, 1)], [(1, 0), (0, -1), (0, -2)], [(1, 0), (2, 0), (0, -1)], # ㄱ자
         [(1, 0), (1, 1), (2, 1)], [(0, 1), (1, 1), (1, 2)], [(1, 0), (1, -1), (2, -1)], [(0, 1), (-1, 1), (-1, 2)], # 계단
         [(0, 1), (0, 2), (1, 1)], [(1, 0), (2, 0), (1, 1)], [(0, 1), (0, 2), (-1, 1)], [(1, 0), (2, 0), (1, -1)]] # T

result = 0
for i in range(N):
    for j in range(M):
        result = max(result, tetro((i, j)))
print(result)