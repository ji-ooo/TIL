import sys
sys.stdin = open('4873.txt')

T = int(input())
for tc in range(1, T+1):
    # 문자열 입력, 빈 리스트 생성 > 스택으로 활용
    word = list(map(str, input().strip()))
    word_check = []
    # 문자열 순회하면서 스택의 top과 비교
    # 일치하면 pop, 다르면 append
    for i in word:
        if word_check and word_check[-1] == i:
            word_check.pop()
        else: word_check.append(i)
    print(f'#{tc} {len(word_check)}')