# from intcode import Machine
# from collections import defaultdict

# with open('day13_input.txt') as f:
# 	l = f.readline().split(',')

# l = [int(i) for i in l]

# r = Machine(l)
# r.run()
# o = r.dump_output()

# screen = defaultdict()
# for i in range(int(len(o)/3)):
# 	ii = i*3
# 	screen[(o[ii],o[ii+1])] = o[ii+2]

# vals = list(screen.values())
# blocks = 0
# for v in vals:
# 	if (v==2):
# 		blocks +=1

# print("Part 1: answer is {:d}".format(blocks))

import intcode
import asyncio
import fileinput


class Draw:
    def __init__(self):
        self.blocks = set()
        self.state = 'X'

    async def __call__(self, value):
        if self.state == 'X':
            self.x = value
            self.state = 'Y'
        elif self.state == 'Y':
            self.y = value
            self.state = 'OUTPUT'
        elif self.state == 'OUTPUT':
            if value == 2:
                self.blocks.add((self.x, self.y))
            else:
                self.blocks.discard((self.x, self.y))
            self.state = 'X'


class Bot:
    def __init__(self):
        self.ball = None
        self.paddle = None
        self.score = None
        self.state = 'X'

    async def input(self):
        if self.ball is not None and self.paddle is not None:
            if self.ball < self.paddle:
                return -1
            elif self.ball > self.paddle:
                return 1
        return 0

    async def output(self, value):
        if self.state == 'X':
            self.x = value
            self.state = 'Y'
        elif self.state == 'Y':
            self.y = value
            self.state = 'OUTPUT'
        elif self.state == 'OUTPUT':
            if self.x == -1 and self.y == 0:
                self.score = value
            elif value == 3:
                self.paddle = self.x
            elif value == 4:
                self.ball = self.x
            self.state = 'X'


def part1(lines):
    mem = [int(s.strip()) for s in lines[0].split(',')]
    draw = Draw()
    asyncio.run(intcode.run_async(mem, None, draw))
    return len(draw.blocks)


def part2(lines):
    mem = [int(s.strip()) for s in lines[0].split(',')]
    mem[0] = 2
    bot = Bot()
    asyncio.run(intcode.run_async(mem, bot.input, bot.output))
    return bot.score


parts = (part1, part2)

if __name__ == '__main__':
    lines = list(fileinput.input())

    print(part1(lines))
    print(part2(lines))