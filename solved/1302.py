N = int(input())

book_list = {}
for _ in range(N):
    book = str(input())
    book_list[book] = book_list.setdefault(book, 0) + 1

book_list = list(book_list.items())
book_list.sort(key=lambda x:x[1])
maxi = book_list[-1][1]
maxi_lst = []

for book, cnt in book_list:
    if cnt == maxi:
        maxi_lst.append(book)

maxi_lst.sort()
print(maxi_lst[0])