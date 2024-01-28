import json
from pprint import pprint


def books_info(books, categories):
    book_list = []
    for book in books:
        new_dict = {}
        want_info = ['id', 'title', 'author', 'priceSales', 'description', 'cover', 'categoryId']
        for i in want_info:
            new_dict[i] = book[i]
            
        cat_list = []
        for category in new_dict['categoryId']:
            for dict in categories:
                if dict['id'] == category:
                    cat_list.append(dict['name'])
        new_dict['categoryId'] = cat_list
        book_list.append(new_dict)
    return book_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
