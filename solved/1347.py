N = int(input())
line = list(map(str, input()))
print(line)

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
direction = 0
x, y = 0, 0
visited = [(x, y)]
max_x, min_x = x, x
max_y, min_y = y, y
for cmd in line:
    if cmd == 'R':
        direction += 1
        if direction == 4:
            direction = 0
    elif cmd == 'L':
        direction -= 1
        if direction == -1:
            direction = 3
    elif cmd == 'F':
        arr, col = directions[direction]
        x += arr
        y += col
        visited.append((x, y))
    max_x = max(max_x, x)
    min_x = min(min_x, x)
    max_y = max(max_y, y)
    min_y = min(min_y, y)
    
    max_arr = max(abs(max_x-min_x), abs(max_y-min_y))
print(max_arr, visited)


