import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def part1():
    from collections import Counter

    def get_score(x):
        match [count for _, count in Counter(x).most_common()]:
            case 5, *_:     
                return 1
            case 4, *_:     
                return 2
            case 3, 2, *_:  
                return 3
            case 3, *_:     
                return 4
            case 2, 2, *_:  
                return 5
            case 2, *_:     
                return 6
            case _:         
                return 7

    order = "AKQJT98765432"
    vals = []
    data = open('input7.txt').read().splitlines()
    for line in data:
        cards, pts = line.split()
        vals.append((get_score(cards), [order.index(x) for x in cards], int(pts)))

    vals.sort(reverse=True)
    return sum((i + 1) * v[-1] for i, v in enumerate(vals))

def part2():
    from collections import Counter
    from itertools import product

    def get_score(x):
        match [count for _, count in Counter(x).most_common()]:
            case 5, *_:
                return 1
            case 4, *_:
                return 2
            case 3, 2, *_:
                return 3
            case 3, *_:
                return 4
            case 2, 2, *_:
                return 5
            case 2, *_:
                return 6
            case _:
                return 7

    order = "AKQT98765432J"
    vals = []
    data = open('input7.txt').read().splitlines()
    for line in data:
        cards, pts = line.split()
        score = get_score(cards)
        for subs in product(order[:-1], repeat=cards.count("J")):
            score = min(score, get_score(cards.replace("J", "") + "".join(subs)))
        vals.append((score, [order.index(x) for x in cards], int(pts)))

    vals.sort(reverse=True)
    return sum((i + 1) * v[-1] for i, v in enumerate(vals))

result_part1 = part1()
result_part2 = part2()

print("Part 1:", result_part1)
print("Part 2:", result_part2)
