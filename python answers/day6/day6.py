import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def part1():
    data = open('input6.txt').read().splitlines()
    data = [x.split() for x in data]
    races = []
    for i in range(1, len(data[0])):
        races.append([int(data[0][i]), int(data[1][i])])

    wins = 0
    ans = 1
    for r in races:
        for btn in range(0, r[0]):
            dist = (r[0] - btn) * btn
            if dist > r[1]:
                wins += 1
        ans *= wins
        wins = 0
    return ans

def part2():
    input_file = open('input6.txt', 'r')
    lines = input_file.readlines()

    time = int(''.join(lines[0].split()[1:]))
    dist = int(''.join(lines[1].split()[1:]))

    total = 0
    for t in range(1, time + 1):
        if t * (time - t) > dist:
            total += 1
    return total


result_part1 = part1()
result_part2 = part2()


print("Part 1:", result_part1)
print("Part 2:", result_part2)
