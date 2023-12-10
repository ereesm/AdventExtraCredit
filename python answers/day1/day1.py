import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#part1
def part1():
    with open("input.txt") as file:
        lines = file.read().splitlines()

    result = 0
    for line in lines:
        digits = [c for c in line if c.isdigit()]
        result += int(digits[0] + digits[-1])

    return result
    
#part2
def part2():
    lines = open("input.txt").read().splitlines()
    p = 0
    for line in lines:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    digits.append(str(d + 1))
        p += int(digits[0] + digits[-1])

    return p


result_part1 = part1()
result_part2 = part2()


print("Part 1:", result_part1)
print("Part 2:", result_part2)