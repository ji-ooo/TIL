import sys
input = sys.stdin.readline

K, L = map(int, input().split())

st_dict = {}
for i in range(L):
    st_id = input().strip()
    st_dict[st_id] = i

st_lst = list(st_dict.items())
st_lst.sort(key= lambda x:x[1])

if len(st_lst) >= K:
    for i in range(K):
        print(st_lst[i][0])
else:
    for i in range(len(st_lst)):
        print(st_lst[i][0])