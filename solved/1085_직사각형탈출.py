x, y, w, h = map(int, input().split())

X = min(abs(x-w), x)
Y = min(abs(y-h), y)
print(min(X, Y))