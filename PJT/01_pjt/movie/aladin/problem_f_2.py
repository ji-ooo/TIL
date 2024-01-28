import json


def sorted_cs_books_by_price(books, categories):
    # 여기에 코드를 작성합니다.
    com_book = []

    for idx in categories:
        idx['name'] == "컴퓨터 공학"
        find_id = idx['id']
    
    for book in books:
        book_id = book['id']
        book = open(f'data/books/{book_id}.json', encoding='utf-8')
        book_detail = json.load(book)  

        category = book_detail['categoryId']
        title = book_detail['title']
        sales = book_detail['priceSales']

        if type(category) == list:
            if find_id in category:
                com_book.append((title, sales))
            
        else:
            if category == find_id:
                com_book.append((title, sales))
    
    com_book.sort(key = lambda x: -x[1])
    result = []
    for i in com_book:
        result.append(i[0])
    
    return result

        
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
