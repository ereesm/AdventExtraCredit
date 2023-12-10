import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import re
from collections import defaultdict

def part1():
    lines = open("input3.txt").read().splitlines()
    ans = 0
    for i, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            idxs = [(i, m.start() - 1), (i, m.end())]  
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]  
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]  
            count = 0
            for a, b in idxs:
                if 0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] != ".":  
                    count += 1
            if count > 0:
                ans += int(m.group())
    return ans

def part2():
    lines = open("input3.txt").read().splitlines()
    adj = defaultdict(list)
    ans = 0
    for i, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            idxs = [(i, m.start() - 1), (i, m.end())]  
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]  
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]  
            for a, b in idxs:
                if 0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] == "*":  
                    adj[a, b].append(m.group())
    for v in adj.values():
        if len(v) == 2:  
            ans += int(v[0]) * int(v[1])
    return ans


result_part1 = part1()
result_part2 = part2()


print("Part 1:", result_part1)
print("Part 2:", result_part2)