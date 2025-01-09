num = []

for i in range(3):
    n = input()
    if n.isdecimal():
        num.append((i, int(n)))

target = num[0][1] + 3 - num[0][0]

if target%3 == 0:
    if target%5 == 0:
        exit(print("FizzBuzz"))
    exit(print("Fizz"))

if target%5 == 0:
    exit(print("Buzz"))

print(target)
        