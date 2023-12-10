import os

def read_input(file_name):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    return open(file_name).read().split('\n\n')

def translate_seeds(seeds, mappings):
    seeds = seeds.split(": ")[1]
    seeds = [int(x) for x in seeds.split()]

    for m in mappings:
        _, *ranges = m.splitlines()
        ranges = [[int(x) for x in r.split()] for r in ranges]
        ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]

        def translate(x):
            for a, b in ranges:
                if x in b:
                    return a.start + x - b.start
            return x

        seeds = [translate(x) for x in seeds]

    return min(seeds)

def find_min_start(seeds, mappings):
    def pairs(l):
        it = iter(l)
        return zip(it, it)

    seeds = seeds.split(": ")[1]
    seeds = [int(x) for x in seeds.split()]
    seeds = [range(a, a + b) for a, b in pairs(seeds)]

    for m in mappings:
        _, *ranges = m.splitlines()
        ranges = [[int(x) for x in r.split()] for r in ranges]
        ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]

        new_seeds = []
        for r in seeds:
            for tr, fr in ranges:
                offset = tr.start - fr.start
                if r.stop <= fr.start or fr.stop <= r.start:
                    continue
                ir = range(max(r.start, fr.start), min(r.stop, fr.stop))
                lr = range(r.start, ir.start)
                rr = range(ir.stop, r.stop)
                if lr:
                    seeds.append(lr)
                if rr:
                    seeds.append(rr)
                new_seeds.append(range(ir.start + offset, ir.stop + offset))
                break
            else:
                new_seeds.append(r)
        seeds = new_seeds

    return min(x.start for x in seeds)

input_file = "input5.txt"
input_data = read_input(input_file)
seeds, mappings = input_data[0], input_data[1:]

result_part1 = translate_seeds(seeds, mappings)
print(result_part1)

result_part2 = find_min_start(seeds, mappings)
print(result_part2)
