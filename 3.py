import re, math
INPUTF = "in3.txt"

def part1(dat):
    return sum([ int(x.group(1)) * int(x.group(2)) for x in re.finditer(r"mul\((\d+),(\d+)\)", dat) ])

def part2(dat):
    enabled = True
    ret = 0
    PATSTR = r"^mul\((\d+),(\d+)\)"

    for start in range(len(dat)):
        cmd = dat[start:]
        if cmd.startswith("do()"):
            enabled = True
        elif cmd.startswith("don't()"):
            enabled = False
        elif enabled and re.match(PATSTR, cmd):
            tmp = re.search(PATSTR, cmd)
            ret += math.prod(map(int, tmp.groups()))

    return ret


with open(INPUTF, 'r') as f:
    dat = f.read()
    p1 = part1(dat)
    p2 = part2(dat)
    print(p1, p2)
