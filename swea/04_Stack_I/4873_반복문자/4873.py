import sys
sys.stdin = open('4873.txt')

T = int(input())
for tc in range(1, T+1):
    word = list(map(str, input().strip()))
    word_check = []
    for i in word:
        if word_check and word_check[-1] == i:
            word_check.pop()
        else: word_check.append(i)
    print(f'#{tc} {len(word_check)}')