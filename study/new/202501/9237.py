N = int(input())
trees = list(map(int, input().split()))

com = []

trees.sort(reverse=True)

for i in range(N):
    com.append(trees[i]+ i+2)
print(max(com))
