## advent of code 2022
## https://adventofcode.com/2022
## day 05
import re
import copy

def parse_input(lines):
    stacks = []
    instructions = []
    while lines:
        l = lines.pop(0)
        if '[' in l:
            print(l)
            l = re.sub(r'\[(.)\] ', '\\1x', l)
            l = re.sub(r'    ', 'x', l)
            l = re.sub(r'\[(.)\]', '\\1', l)
            l = re.sub(r'([A-Z]).', '\\1', l)
            stacks.append(l)
        elif 'move' in l:
            l = [int(x) for x in re.sub(r'move |from |to ', '', l).split()]
            instructions.append(l)

    towers = [ []*9 for i in range(9) ]
    for i in reversed(range(len(stacks))):
        tower = []
        for y in range(9):
            if stacks[i][y] != 'x':
                towers[y].append(stacks[i][y])
    return [towers, instructions]

def print_towers(towers):
    print('----------')
    for t in towers:
        print(''.join(t))
    print('----------')

def get_top_crate(tower):
    return tower.pop()

def get_top_crates(towers):
    crates = []
    for t in towers:
        crates.append(get_top_crate(t))
    return ''.join(crates)

def part1(data):
    towers = copy.deepcopy(data[0])
    instructions = data[1]

    for i in instructions:
        amount = i[0]
        origin = i[1] - 1
        dest = i[2] - 1

        #print('move {} from {} to {}'.format(amount, origin, dest))
        #print_towers(towers)
        for ci in range(amount):
            crate = towers[origin].pop()
            towers[dest].append(crate)
        #print_towers(towers)
    return get_top_crates(towers)

def part2(data):
    towers = copy.deepcopy(data[0])
    instructions = data[1]

    for i in instructions:
        amount = i[0]
        origin = i[1] - 1
        dest = i[2] - 1

        #print('move {} from {} to {}'.format(amount, origin, dest))
        #print_towers(towers)
        crates = towers[origin][len(towers[origin])-amount:]
        towers[origin] = towers[origin][:-amount]
        #print(crates)
        towers[dest].extend(crates)
        #print_towers(towers)
    return get_top_crates(towers)
