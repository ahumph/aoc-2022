## advent of code 2022
## https://adventofcode.com/2022
## day 10
import math

def parse_input(lines):
    #with open('2022/10/example_input.txt', 'r') as f:
    #    lines = f.read().split("\n")[:-1]
    return [(l.split()[0], int(l.split()[1]) if ' ' in l else None) for l in lines]

def part1(data):
    x = 1
    cycle = 1
    signal = [0]
    for op, n in data:
        signal.append(x*cycle)
        if op == 'addx':
            cycle += 1
            signal.append(x*cycle)
            x += n
        cycle += 1
    return sum([signal[i] for i in [20,60,100,140,180,220]])

def get_lines(screen):
    for i in range(0, len(screen), 40):
        yield screen[i:i+40]

def print_screen(screen):
    li = 1
    for line in get_lines(screen):
        print("Cycle {:>3} -> {} <- Cycle {:>3}".format(str(li), ''.join(line), str(li+40)))
        li += 40

def part2(data):
    x = 1
    cycle = 1
    crt = []
    for op, n in data:
        crt.append('#' if abs(x-(cycle%40)+1) <=1 else '.')
        if op == 'addx':
            cycle += 1
            crt.append('#' if abs(x-(cycle%40)+1) <=1 else '.')
            x += n
        cycle += 1
    print_screen(crt)
    return 'EZFPRAKL'
