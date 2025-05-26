import sys
input = sys.stdin.readline

N = int(input())
words = list(input().strip() for _ in range(N))
sc = [0] * 26

ans = []

for word in words:
    wl = word.split()
    res = word

    for i, w in enumerate(wl):
        ws = w[0].upper()
        wc = ord(ws) - 65

        if not sc[wc]:
            sc[wc] = 1
            wl[i] = '[' + w[0] + ']' + w[1:]
            res = ' '.join(wl)
            break

    else:
        for i, c in enumerate(word):
            if c.isalpha():
                cu = c.upper()
                cc = ord(cu) - 65

                if not sc[cc]:
                    sc[cc] = 1
                    res = word[:i] + '[' + c + ']' + word[i+1:]
                    break

    ans.append(res)
    
for a in ans:
    print(a)
