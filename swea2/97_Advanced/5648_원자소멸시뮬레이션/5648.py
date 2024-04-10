import sys
sys.stdin = open('5648.txt')

for tc in range(1, int(input())+1):
    N = int(input())

    atoms = []

    for _ in range(N):
        x, y, d, k = map(int, input().split())
        x *= 2
        y *= 2
        atoms.append([x, y, d, k])

    result = 0
    while len(atoms) >= 2:
        tmp = []
        crash = []
        out = []
        for atom in atoms:
            d = atom[2]

            if d == 0:
                atom[1] += 1
            elif d == 1:
                atom[1] -= 1
            elif d == 2:
                atom[0] -= 1
            elif d == 3:
                atom[0] += 1

            if atom[0] < -2000 or atom[0] > 2000:
                out.append(atom)
            elif atom[1] < -2000 or atom[1] > 2000:
                out.append(atom)
            else:
                if (atom[0], atom[1]) in tmp:
                    crash.append((atom[0], atom[1]))
                else:
                    tmp.append((atom[0], atom[1]))

        for atom in atoms:
            if (atom[0], atom[1]) in crash:
                result += atom[3]
                out.append(atom)

        for atom in out:
            atoms.remove(atom)

    print(f'#{tc} {result}')
