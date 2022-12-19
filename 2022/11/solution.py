## advent of code 2022
## https://adventofcode.com/2022
## day 11
import re
import math

class Monkey:
    def __init__(self, id, op, test, throw, items):
        self.id = id
        self.items = []
        self.items.extend(items)
        self.operation = op[0]
        self.operand = op[1]
        self.test = test
        self.throw_true = throw[0]
        self.throw_false = throw[1]
        self.inspections = 0

    def __repr__(self):
        return 'Monkey {}'.format(self.id)

    def __str__(self):
        string = 'Monkey {}\n'.format(self.id)
        string += '  Starting items: {}\n'.format(', '.join([str(x) for x in self.items]))
        string += '  Operation: new = old {} {}\n'.format(self.operation, self.operand)
        string += '  Test: divisible by {}\n'.format(self.test)
        string += '    If true: throw to monkey {}\n'.format(self.throw_true)
        string += '    If false: throw to monkey {}\n'.format(self.throw_false)
        return string

    def op(self, item):
        if self.operation == '+':
            return item + self.operand
        elif self.operation == '**':
            return item * item
        elif self.operation == '*':
            return item * self.operand

    def inspect(self, worry=False):
        #print('Monkey {}'.format(str(self.id)))
        for i, item in enumerate(self.items):
            #print(' Monkey inspects an item with a worry level of {}'.format(str(item)))
            #print('  Worry level is multiplied by {} to {}'.format(str(self.operand), str(self.op(item))))
            new = int(self.op(item))
            if not worry:
                new = int(new / 3)
            else:
                new = new % self.lcm
            self.items[i] = new
            self.inspections += 1

    def throw(self):
        results = []
        for i in self.items:
            if i % self.test:
                results.append((i, self.throw_false))
                #print('  Item with worry level {} is thrown to monkey {}'.format(str(i), str(self.throw_false)))
            else:
                results.append((i, self.throw_true))
                #print('  Item with worry level {} is thrown to monkey {}'.format(str(i), str(self.throw_true)))
        self.items = []
        return results
    
    def empty(self):
        return len(self.items) == 0


def parse_input(lines):
    lines = '\n'.join(lines).split("\n\n")
    #with open('2022/11/example_input.txt', 'r') as f:
    #    lines = f.read().split("\n\n")
    monkeys = []
    for i, m in enumerate(lines):
        items = []
        op = None
        operand = None
        divisible = None
        throw_true = None
        throw_false = None
        for line in m.split("\n"):
            if 'Starting items' in line:
                items.extend([int(x) for x in re.findall(r'\d+\.?\d*', line)])
            elif 'Operation' in line:
                if '+' in line:
                    op = '+'
                    operand = int(re.findall(r'\d+', line)[0])
                elif 'old * old' in line:
                    op = '**'
                elif '*' in line:
                    op = '*'
                    operand = int(re.findall(r'\d+', line)[0])
            elif 'Test' in line:
                divisible = int(re.findall(r'\d+', line)[0])
            elif 'true:' in line:
                throw_true = int(re.findall(r'\d+', line)[0])
            elif 'false:' in line:
                throw_false = int(re.findall(r'\d+', line)[0])
        monkeys.append(Monkey(i, (op, operand), divisible, (throw_true, throw_false), items))

        divisors = []
        for m in monkeys:
            divisors.append(m.test)
        lcm = math.lcm(*divisors)
        for m in monkeys:
            m.lcm = lcm
    return monkeys

def part1(data):
    return 0
    #monkeys = data
    #for r in range(20):
    #    print('Round {}'.format(r+1))
    #    new_items = []
    #    for m in monkeys:
    #        if m.empty():
    #            continue
    #        m.inspect()
    #        for i, new_m in m.throw():
    #            #print(' {} to monkey {}'.format(str(i), str(new_m)))
    #            monkeys[new_m].items.append(i)
    #    for m in monkeys:
    #        print('{}: {}'.format(repr(m), m.items))

    #    for m in monkeys:
    #        print('{} inspected items {} times.'.format(repr(m), str(m.inspections)))

    #    monkey_business = sorted([m.inspections for m in monkeys])
    #    monkey_business = math.prod(monkey_business[-2:])
    #return monkey_business

def part2(data):
    monkeys = data
    for r in range(10000):
        #print('Round {}'.format(r+1))
        new_items = []
        for m in monkeys:
            if m.empty():
                continue
            m.inspect(worry=True)
            for i, new_m in m.throw():
                #print(' {} to monkey {}'.format(str(i), str(new_m)))
                monkeys[new_m].items.append(i)

        if (r+1) % 1000 == 0 or (r+1) == 20:
            print('== After round {} =='.format(str(r+1)))
            for m in monkeys:
                print('{} inspected items {} times.'.format(repr(m), str(m.inspections)))

        monkey_business = sorted([m.inspections for m in monkeys])
        monkey_business = math.prod(monkey_business[-2:])
    return monkey_business
