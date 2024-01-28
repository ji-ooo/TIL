import json
from pprint import pprint


def book_info(book, categories):
    # 여기에 코드를 작성합니다.
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
        
    return new_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
