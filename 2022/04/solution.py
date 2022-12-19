## advent of code 2022
## https://adventofcode.com/2022
## day 04
import time
import re

def parse_input(lines):
    pairs = [l.split(',') for l in lines]
    return pairs

def part1(data):
    st = time.time()
    contained = 0
    for pair in data:
        #a, b, c, d = map(int, re.findall('\d+', pair))
        #if a <= c and b >= d or c <= a and d >= b:
        #    contained += 1
        elf1 = [int(x) for x in pair[0].split('-')]
        elf2 = [int(x) for x in pair[1].split('-')]
        if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            contained += 1
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
            contained += 1
    print('Part 1 execution time:', time.time()-st)
    return contained

def part2(data):
    st = time.time()
    cache = {}
    overlap = 0
    #data = [','.join(x) for x in data]
    for pair in data:
        #a, b, c, d = map(int, re.findall('\d+', pair))
        #if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
        #    overlap += 1
        elf1 = [int(x) for x in pair[0].split('-')]
        elf2 = [int(x) for x in pair[1].split('-')]
        for id in range(elf1[0], elf1[1] + 1):
            if id not in cache:
                cache[id] = 1
        for id in range(elf2[0], elf2[1] + 1):
            if id in cache:
                overlap += 1
                break
        cache = {}
    print('Part 2 execution time:', time.time()-st)
    return overlap
