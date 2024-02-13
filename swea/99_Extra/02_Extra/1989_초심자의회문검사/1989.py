import sys
sys.stdin = open('1989.txt')

T = int(input())

for tc in range(1, T+1):
    word = str(input())

    ans = 0
    for i in range(len(word)//2):
        if word[i] != word[-(i + 1)]:
            break
    else:
        ans = 1

    print(f'#{tc} {ans}')