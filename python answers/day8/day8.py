import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from itertools import cycle
import math

def part1(instr, data):
    data = [x.split(" = ") for x in data.splitlines()]
    data = {a: b[1:-1].split(", ") for a, b in data}

    curr = "AAA"
    for count, d in enumerate(cycle(instr), start=1):
        curr = data[curr][d == "R"]
        if curr == "ZZZ":
            return count

def part2(instr, data):
    data = [x.split(" = ") for x in data.splitlines()]
    data = {a: b[1:-1].split(", ") for a, b in data}

    ans = []
    for curr in data:
        if not curr.endswith("A"):
            continue
        visited = set()
        for count, (idx, d) in enumerate(cycle(enumerate(instr)), start=1):
            prev, curr = curr, data[curr][d == "R"]
            visited.add((curr, idx))
            if prev.endswith("Z") and (curr, idx) in visited:
                ans.append(count - 1)
                break
    return math.lcm(*ans)

# Read input
instr, data = open('input8.txt').read().split("\n\n")

# Run the functions
result_part1 = part1(instr, data)
result_part2 = part2(instr, data)

# Print the results
print("Part 1:", result_part1)
print("Part 2:", result_part2)
