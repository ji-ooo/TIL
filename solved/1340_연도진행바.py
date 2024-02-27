M, D, Y, T = map(str, input().split())
D = int(D[:-1])
Y = int(Y)
H, mm = map(int, T.split(':'))

year = 365
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m_d = [0, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
day = 0

i = 1
while M != m_d[i]:
    i += 1
M = i

if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0):
        year += 1
        month[2] += 1

for i in range(1, 13):
    if M == i:
        for j in range(1, i):
            day += month[j]
day += D-1

total = day * 24 * 60 + H * 60 + mm
total_mm = year * 24 * 60
result = total / total_mm *100

print(result)
    