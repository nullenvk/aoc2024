INPUTF = "in1.txt"

a, b = [], []

with open(INPUTF, 'r') as f:
    for line in f:
        ina, inb = map(int, line.split())
        a.append(ina)
        b.append(inb)

a.sort()
b.sort()

part1 = sum([abs(x - y) for (x,y) in zip(a, b)])
part2 = sum([x * b.count(x) for x in a])

print("A:", part1, "B:", part2)
