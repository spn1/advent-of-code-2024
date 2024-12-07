import csv

levels = []

with open('./input.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        numbers = row[0].split(' ')
        levels.append(row)


def is_level_safe(level):
    is_safe = True
    levels = list(map(lambda n: int(n), level.split(' ')))
    is_increasing_or_decreasing = \
        levels == sorted(levels) or levels == sorted(levels, reverse=True) 
    
    if not is_increasing_or_decreasing:
        return False

    for i in range(len(levels) - 1):
        current = int(levels[i])
        next = int(levels[i+1])

        is_safe = \
            current != next and \
            abs(current - next) <= 3

        if is_safe == False: break

    return is_safe


def part_one():
    safe_report_count = 0
    for level in levels:
        if is_level_safe(level[0]): safe_report_count += 1

    return safe_report_count


def part_two():
    pass


if __name__ == '__main__':
    print(part_one())
    print(part_two())