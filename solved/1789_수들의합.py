S = int(input())

i = 1
cnt = 0
while S > 0:
    S -= i
    cnt += 1
    i += 1

if S < 0:
    cnt -= 1
print(cnt)