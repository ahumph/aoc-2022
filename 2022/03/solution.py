## advent of code 2022
## https://adventofcode.com/2022
## day 03

def parse_input(lines):
    return lines

def get_priority(ch):
    if ch.islower():
        return ord(ch)-96
    else:
        return ord(ch)-38

def part1(data):
    data = [(l[:round(len(l)/2)], l[round(len(l)/2):]) for l in data]
    doubles = []
    for rucksack in data:
        cache = {}
        for item in rucksack[0]:
            if item not in cache:
                cache[item] = 1
        for item in rucksack[1]:
            if item in cache:
                doubles.append(item)
                break
    return sum([get_priority(d) for d in doubles])

def part2(data):
    data = zip(*(iter(data),) * 3)
    triples = []
    for group in data:
        cache = {}
        for item in group[0]:
            if item not in cache:
                cache[item] = 1
        for item in group[1]:
            if item in cache and cache[item] == 1:
                cache[item] += 1
                group[1].replace(item,'')
        for item in group[2]:
            if item in cache and cache[item] == 2:
                triples.append(item)
                break
    return sum([get_priority(d) for d in triples])
