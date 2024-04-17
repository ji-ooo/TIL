n, m = map(int, input().split())
cards = list(map(int, input().split()))

while m:
    cards.sort(reverse=True)
    c, d = cards[-2:]
    s = c + d
    cards[-2] = cards[-1] = s
    m -= 1
print(sum(cards))
