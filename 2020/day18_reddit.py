# https://www.reddit.com/r/adventofcode/comments/kfeldk/2020_day_18_solutions/gg8uew3/?utm_source=reddit&utm_medium=web2x&context=3

from collections import deque as deque

def parseHomework1(maths):
    if isinstance(maths,str):
        while "(" in maths:
            deepest = None
            for i in range(len(maths)):
                if maths[i] == "(":
                    deepest = i
                if maths[i] == ")":
                    maths = maths[:deepest] + parseHomework1(maths[deepest+1:i]) + maths[i+1:]
                    break
        maths = deque(maths.split(" "))
    while len(maths) != 1:
        a = int(maths.popleft())
        op = maths.popleft()
        b = int(maths.popleft())
        if op == "*":
            maths.insert(0,str(a * b))
        elif op == "+":
            maths.insert(0,str(a + b))
    return maths[0]

def part1():
    f = [e.rstrip() for e in open("day18_input.txt")]
    res = 0
    for line in f:
        res += int(parseHomework1(line))
    return res

print(part1())

def parseHomework2(maths):
    if isinstance(maths,str):
        while "(" in maths:
            deepest = None
            for i in range(len(maths)):
                if maths[i] == "(":
                    deepest = i
                if maths[i] == ")":
                    maths = maths[:deepest] + parseHomework2(maths[deepest+1:i]) + maths[i+1:]
                    break
        maths = deque(maths.split(" "))
    while "+" in maths:
        plusPos = maths.index("+")
        a = int(maths[plusPos-1])
        b = int(maths[plusPos+1])
        maths[plusPos] = str(a + b)
        del maths[plusPos + 1]
        del maths[plusPos - 1]
    while len(maths) != 1:
        a = int(maths.popleft())
        op = maths.popleft()
        b = int(maths.popleft())
        if op == "*":
            maths.insert(0,str(a * b))
        elif op == "+":
            assert False
    return maths[0]

def part2():
    f = [e.rstrip() for e in open("day18_input.txt")]
    res = 0
    for line in f:
        res += int(parseHomework2(line))
    return res

print(part2())
