## advent of code 2022
## https://adventofcode.com/2022
## day 06
import time, re

def parse_input(lines):
    return lines[0]

def find_marker(data, n):
    s = time.time()
    match = 0
    i = 0
    while not match:
        chars = data[i:i+n]
        if len(chars) == len(set(chars)):
            match = 1
        else:
            i += 1
    print('Execution time:', time.time()-s)
    return i+n

def build_regex(n):
    regex = "(.)"
    for i in range(1, n):
        regex += "(?!"
        for j in range(1, i+1):
            regex += f"\\{j}"
            if j < i:
                regex += "|"
        regex += ")." if i == n-1 else ")(.)"
    return regex

def part1(data):
    s = time.time()
    r = re.search(build_regex(4), data).span()[1]
    print('Part 1 Executed in:', time.time()-s)
    return r

def part2(data):
    s = time.time()
    r = re.search(build_regex(14), data).span()[1]
    print('Part 2 Executed in:', time.time()-s)
    return r
