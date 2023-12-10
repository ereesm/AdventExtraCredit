import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from itertools import pairwise

def part1_logic(data):
    def seq(ints):
        if all(ints == 0 for ints in ints):
            return 0
        diffs = [b - a for a, b in pairwise(ints)]
        return ints[-1] + seq(diffs)

    ans = 0
    for d in data:
        ans += seq([int(x) for x in d.split()])
    return ans

def part2_logic(data):
    def seq(ints):
        if all(ints == 0 for ints in ints):
            return 0
        diffs = [b - a for a, b in pairwise(ints)]
        return ints[-1] + seq(diffs)

    ans = 0
    for d in data:
        ans += seq([int(x) for x in d.split()[::-1]])
    return ans

# Read input
data = open('input9.txt').read().splitlines()

# Run the functions
result_part1 = part1_logic(data)
result_part2 = part2_logic(data)

# Print the results
print("Part 1:", result_part1)
print("Part 2:", result_part2)
