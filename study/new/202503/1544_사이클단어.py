def sol(w1, w2):
    if len(w1) != len(w2):
        return False
    
    return w2 in w1 + w1

n = int(input())
words = []
for _ in range(n):
    words.append(input())

word_set = set()
cnt = 0

for i in range(n):
    if i in word_set:
        continue

    cnt += 1

    for j in range(i + 1, n):
        if j not in word_set and sol(words[i], words[j]):
            word_set.add(j)

print(cnt)