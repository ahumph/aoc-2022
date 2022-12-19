## advent of code 2022
## https://adventofcode.com/2022
## day 09

class P:
    dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tuple(self):
        return self.x, self.y

    def move(self, d):
        self.x += P.dirs[d][0]
        self.y += P.dirs[d][1]

    def follow(self, p):
        dx = p.x - self.x
        dy = p.y - self.y
        if abs(dx) > 1:
            self.x += 1 if dx > 0 else -1
            if abs(dy) == 1:
                self.y += dy
        if abs(dy) > 1:
            self.y += 1 if dy > 0 else -1
            if abs(dx) == 1:
                self.x += dx

def parse_input(lines):
    with open('2022/09/grid.txt', 'r') as f:
        grid = f.read().split("\n")[:-1]
    #with open('2022/09/example_input.txt', 'r') as f:
    #    lines = f.read().split("\n")[:-1]
    grid = [[x for x in l] for l in grid]
    size_x = len(grid[0])
    size_y = len(grid)
    x = 0
    index = 0
    for l in grid:
        if 'H' in l:
            x = index
            y = l.index('H')
        index += 1
    instructions = [[x.split()[0], int(x.split()[1])] for x in lines]
    moves = [(dir, int(steps)) for dir, steps in (line.split() for line in lines)]
    print(moves)
    return moves

def part1(data):
    rope = [P(0,0) for _ in range(10)]
    v1 = {rope[1].tuple()}
    v2 = {rope[-1].tuple()}
    for dir, steps in data:
        for step in range(steps):
            rope[0].move(dir)
            for i in range(1, len(rope)):
                rope[i].follow(rope[i-1])
            v1.add(rope[1].tuple())
            v2.add(rope[-1].tuple())
    print(v1)
    print(len(v1))
    return len(v1)

def part2(data):
    rope = [P(0,0) for _ in range(10)]
    v1 = {rope[1].tuple()}
    v2 = {rope[-1].tuple()}
    for dir, steps in data:
        for step in range(steps):
            rope[0].move(dir)
            for i in range(1, len(rope)):
                rope[i].follow(rope[i-1])
            v1.add(rope[1].tuple())
            v2.add(rope[-1].tuple())
    print(v2)
    print(len(v2))
    return len(v2)
