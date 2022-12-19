# parse lines of input
import sys

def parse():
    ex = sys.argv[1] if len(sys.argv) > 1 else None
    fn = "example_input.txt" if ex else "input.txt"
    with open(fn, "r") as f:
        return list(filter(None, f.read().split("\n")[:-1]))
