import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#part1
def part1():
    data = open("input2.txt").read().splitlines()
    data = [x.replace(',', '') for x in data]
    data = [x.split(';') for x in data]
    ans = 0
    round = 1
    for d in data:
        for e in d:
            r, g, b = 0, 0, 0
            prev = 0
            possible = True
            ff = e.split(' ')
            for f in ff:
                match f:
                    case 'red':
                        r += int(prev)
                    case 'green':
                        g += int(prev)
                    case 'blue':
                        b += int(prev)
                prev = f
            if r > 12 or g > 13 or b > 14:
                possible = False
                break
        if possible:
            ans += round
        round += 1
    return ans



#part 2
def part2():
    data = open("input2.txt").read().splitlines()
    data = [x.replace(',', '') for x in data]
    data = [x.split(';') for x in data]
    ans = 0
    for d in data:
        rmax, gmax, bmax = 0, 0, 0
        for e in d:
            r, g, b = 0, 0, 0
            prev = 0
            ff = e.split(' ')
            for f in ff:
                match f:
                    case 'red':
                        r += int(prev)
                    case 'green':
                        g += int(prev)
                    case 'blue':
                        b += int(prev)
                prev = f
            if r > rmax:
                rmax = r
            if g > gmax:
                gmax = g
            if b > bmax:
                bmax = b
        ans += rmax * gmax * bmax
    return ans


result_part1 = part1()
result_part2 = part2()


print("Part 1:", result_part1)
print("Part 2:", result_part2)