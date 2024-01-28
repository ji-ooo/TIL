import json


def best_book(books):
    # 여기에 코드를 작성합니다.
    max_review = 0
    result = ''

    for book in books:
        book_id = book['id']
        book = open(f'data/books/{book_id}.json', encoding='utf-8')
        book_detail = json.load(book)

        review = book_detail['customerReviewRank']
        max_review = max(max_review, review)

        if max_review == review:
            result = book_detail['title']

    return result
        
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))
