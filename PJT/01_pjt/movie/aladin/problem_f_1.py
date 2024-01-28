import json


def best_new_books(books):
    # 여기에 코드를 작성합니다.
    new_list = []
    for book in books:
        book_id = book['id']
        book = open(f'data/books/{book_id}.json', encoding='utf-8')
        book_detail = json.load(book)

        pubDate = book_detail['pubDate']
        pubYear = pubDate[:4]

        if pubYear == '2023':
            new_list.append((book_detail['title'], book_detail['customerReviewRank']))
    new_list.sort(key = lambda x: x[1])

    return new_list[-1][0]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_new_books(books_list))
