from queue import PriorityQueue
a, b = map(int, input().split())
dp = PriorityQueue()
cnt = 1
dp.put((a, cnt))
a1 = a2 = a

result = 0
while a1 <= b or a2 <= b:
    now = dp.get()
    a, cnt = now
    cnt += 1
    a1 = a*2
    a2 = int(str(a)+'1')
    if a1 == b or a2 == b:
        result = cnt
        break
    else:
        dp.put((a1, cnt))
        dp.put((a2, cnt))

if result:
    print(result)
else:
    print(-1)