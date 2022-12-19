## advent of code 2022
## https://adventofcode.com/2022
## day 08
import math

def parse_input(lines):
    #with open('2022/08/example_input.txt', 'r') as f:
    #    lines = f.read().split("\n")[:-1]
    grid = [[int(x) for x in l] for l in lines]
    return grid

def to_the_edge(x, y, grid, direction):
    if 'n' in direction:
        for p in range(x-1, -1, -1):
            yield grid[p][y]
    elif 's' in direction:
        for p in range(x+1, len(grid)):
            yield grid[p][y]
    elif 'w' in direction:
        for p in range(y-1, -1, -1):
            yield grid[x][p]
    elif 'e' in direction:
        for p in range(y+1, len(grid)):
            yield grid[x][p]

def visible(x, y, grid, direction):
    return grid[x][y] > max(to_the_edge(x, y, grid, direction))

def trees(x, y, grid, direction):
    count = 0
    for h in to_the_edge(x, y, grid, direction):
        count += 1
        if grid[x][y] <= h:
            break
    return count

def print_grid(data):
    for x in range(0, len(data)):
        line = ""
        for y in range(0, len(data)):
            line += str(data[x][y]) + " "
        print(line)

def part1(data):
    v = [[0]*len(data)]*len(data)
    v[0] = [1]*len(data)
    v[len(data)-1] = [1]*len(data)
    for x in range(1, len(data)-1):
        v[x][0] = 1
        v[x][len(data)-1] = 1

    count = len(data)*4 - 4
    for x in range(1,len(data)-1):
        for y in range(1,len(data)-1):
            if any([visible(x, y, data, d) for d in 'nwse']):
                count += 1

    return count

def part2(data):
    best = 0
    for x in range(1, len(data)-1):
        for y in range(1, len(data)-1):
            score = math.prod([trees(x, y, data, d) for d in 'nwse'])
            if score > best:
                best = score
    return best
