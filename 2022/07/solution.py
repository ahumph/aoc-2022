## advent of code 2022
## https://adventofcode.com/2022
## day 07
import re
from itertools import cycle

sizes = {}
tree = {}

def get_size(d, size=None):
    if type(d) == int:
        return d
    s = 0
    for o in d:
        s += get_size(d[o], size)
    if size != None:
        size.append(s)
    return s

def print_tree(tree, indent=1):
    print(tree, indent)
    for key, value in tree.items():
        print('-'*indent, ' {} (dir)'.format(key))
        if isinstance(value, dict):
            print_tree(value, indent+1)
        else:
            print('-'*indent, ' {} (file, size={})'.format(key, value))

def parse_input(lines):
    stack = []
    node = tree
    size = len(lines)
    for items in [l.split() for l in lines]:
        if items[0] == '$':
            if items[1] == 'cd':
                if items[2] == '..':
                    node = stack.pop()
                elif items[2] == '/':
                    node = tree
                else:
                    stack.append(node)
                    node = node[items[2]]
        else:
            if items[0] == 'dir':
                node[items[1]] = {}
            else:
                node[items[1]] = int(items[0])
    return tree

def part1(data):
    size = []
    _ = get_size(data, size)
    return sum([s for s in size if s<100000])
#            if '..' in line:
#                temp = wd
#                wd = ld
#                ld = temp
#            else:
#                ld = wd
#                wd = line.replace('$ cd ', '')
#            if wd not in tree:
#                tree[wd] = {}
#        elif '$ ls' in line:
#            pass
#        elif 'dir' in line:
#            print('dir found', line.split()[1])
#            tree[wd][line.split()[1]] = {}
#        elif re.match(r'[0-9]+', line):
#            print('file found', line.split()[1])
#            tree[wd][line.split()[1]] = int(line.split()[0])

def part2(data):
    size = []
    total = get_size(data, size)
    space = 70000000
    need = 30000000
    for s in sorted(size):
        if space-total+s > need:
            return s
