## advent of code 2022
## https://adventofcode.com/2022
## day 02
import time

outcomes = {
    '12': 6,
    '13': 0,
    '21': 0,
    '23': 6,
    '31': 6,
    '32': 0
}

wins = {
    '1': 2,
    '2': 3,
    '3': 1
}
losses = {
    '1': 3,
    '2': 1,
    '3': 2
}

scores = {
    -2: 6, 1: 6,
    -1: 0, 2: 0,
    0: 3
}

def parse_input(lines):
    rounds = [x.replace('X', '1').replace('Y', '2').replace('Z', '3')
              .replace('A', '1').replace('B', '2').replace('C', '3')
              .split() for x in lines]
    return rounds

def part1(data):
    total_time = time.time()
    score = 0
    for r in data:
        score += int(r[1])
        # draw
        if r[0] == r[1]:
            score += 3
        else:
            score += outcomes[''.join(r)]
    total_time = time.time() - total_time
    print('Part 1 executed in ' + str(total_time))
    return score

def part2(data):
    total_time = time.time()
    score = 0
    for r in data:
        #score += scores[ord(r[1]) - ord(r[0])] + int(r[1])
        if r[1] == '2':
            # end in draw
            score += 3
            score += int(r[0])
        elif r[1] == '3':
            # end in win
            score += 6
            score += wins[r[0]]
        elif r[1] == '1':
            # end in loss
            score += losses[r[0]]
    total_time = time.time() - total_time
    print('Part 2 executed in ' + str(total_time))

    return score
