# N, C, W = map(int, input().split())

# trees = []
# for _ in range(N):
#     trees.append(int(input()))

# result = 0
# length = 10000
# while length > 0:
#     cut = 0
#     cnt = 0
#     for tree in trees:
#         if tree < length:
#             continue

#         tmp = tree//length
#         tmp_cnt = tmp_cut = tmp

#         if tree%length == 0:
#             tmp_cut -= 1
        
#         if tmp_cut*C < tmp_cnt*W*length:
#             cnt += tmp_cnt
#             cut += tmp_cut

#     money = W * length * cnt - C * cut
#     result = max(result, money)
#     length -= 1

# print(result)

N, C, W = map(int,input().split())
woods   = [int(input()) for _ in range(N)]

profit = [] # 각 이득

for i in range(1,max(woods)+1): # 젤 큰 나무까지 순회하면서 자연수 단위로 잘라봄
    cart = [] # 자른거 담을 바구니
    cut  = 0
    total = 0
    for wood in woods: # 나무 하나씩 꺼내서 잘라봄
        cutting_wood = [i] * (wood // i)  # 잘라진 나무 더미
        cart.append(cutting_wood) # 카트로 담아봄
        
    print(cart, i, '----', sep='\n')
    for j in range(len(cart)):
        if len(cart[j]) > 0: # 일단 최소 한덩이는 나왓음
            if woods[j] % i == 0:
                cutting = len(cart[j]) - 1 # 이렇게 만들려고 몇번 잘랐니
                mymoney = sum(cart[j]) * W - (cutting * C) # 그럼 이 바구니 가격 나옴
                total += mymoney
            elif woods[j] % i != 0:
                cutting = len(cart[j])
                mymoney = sum(cart[j]) * W - (cutting * C) # 그럼 이 바구니 가격 나옴
                total += mymoney
    profit.append(total)

print(profit)
print(max(profit))