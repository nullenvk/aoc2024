from itertools import pairwise
INPUTF = "in2.txt"

def partA(dat):
    diffs = [ y - x for x, y in pairwise(dat)]
    comps = [ y > x for x,y in pairwise(dat)]
    return all([abs(x) in [1,2,3] for x in diffs]) and (all(comps) or not any(comps))

def partB(dat):
    return any([partA(dat[0:i] + dat[i+1:]) for i in range(len(dat))])

with open(INPUTF, 'r') as f:
    dat = [ list(map(int, line.split())) for line in f ]
    resA = [ partA(x) for x in dat ].count(True)
    resB = [ partB(x) for x in dat ].count(True)
    print("A", resA, "B", resB)
