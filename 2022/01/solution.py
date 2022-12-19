## advent of code 2022
## https://adventofcode.com/2022
## day 01
import numpy as np

def parse_input(lines):
    lines = [int(x) if x != "" else 0 for x in lines]
    return lines

def part1(data):
    largest = 0
    elf = 0
    for i in data:
        if i > 0:
            elf += i
        else:
            if elf > largest:
                largest = elf
            elf = 0
    return largest

def part2(data):
    elves = []
    elf = 0
    for i in data:
        if i > 0:
            elf += i
        else:
            elves.append(elf)
            elf = 0
    elves.append(elf)
    top3_ids = np.argsort(elves)[-3:]
    top3_vals = [elves[i] for i in top3_ids]
    print(top3_vals)
    print(sum(top3_vals))
    return sum(top3_vals)
