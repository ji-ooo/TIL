N = int(input())

tri = [list(map(int, input().split())) for _ in range(N)]


for i in range(1, N):
    for j in range(len(tri[i])):
        if i == 1:
            tri[i][j] += tri[i-1][0]
        else:
            if j == 0:
                tri[i][j] += tri[i-1][0]
            elif j == len(tri[i])-1:
                tri[i][j] += tri[i-1][j-1]
            else:
                tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])
print(max(tri[-1]))
        

# def find_mx(r, i, tmp_ans):
#     global result

#     if r == N:
#         result = max(result, tmp_ans)
    
#     else:
#         find_mx(r+1, i, tmp_ans + tri[r][i])
#         find_mx(r+1, i+1, tmp_ans + tri[r][i])

# result = 0
# find_mx(0, 0, 0)

'''
위에 삼각형 값을 계속 더해주다가
마지막 줄에서 max 뽑으면 됨
'''