import os

def read_input(file_name):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    data = open(file_name).read().splitlines()
    return [x.split('|') for x in data]

def calculate_points(cards, wins):
    points = 0
    ans = 0
    first_win = True

    for i, card in enumerate(cards):
        for num in card:
            if num in wins[i]:
                if first_win:
                    points += 1
                    first_win = False
                else:
                    points *= 2
        ans += points
        points = 0
        first_win = True

    return ans

def calculate_total_duplicates(cards, wins):
    dups = [1 for _ in cards]

    for i, card in enumerate(cards):
        hit_count = 0
        for num in card:
            if num in wins[i]:
                hit_count += 1
                dups[i + hit_count] += dups[i]

    return sum(dups)

# Example usage:
input_file = "input4.txt"
data = read_input(input_file)

wins = [x[0][10:].strip().split() for x in data]
cards = [x[1].strip().split() for x in data]

# Part 1
result_part1 = calculate_points(cards, wins)
print(result_part1)

# Part 2
result_part2 = calculate_total_duplicates(cards, wins)
print(result_part2)
