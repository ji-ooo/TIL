N = int(input())
crs = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

crs.sort(reverse=True)
boxes.sort(reverse=True)

if crs[0] < boxes[0]:
    exit(print(-1))

t = 0

while boxes:
    for cr in crs:
        if boxes and cr < boxes[-1]:
            continue

        for box in boxes:
            if cr >= box:
                boxes.remove(box)
                break
    t += 1
    
print(t)