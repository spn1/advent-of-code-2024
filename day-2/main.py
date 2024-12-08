import csv
import functools

input = []

with open('./input.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        numbers = row[0].split(' ')
        input.append(row)


def is_level_safe(current, next):
    is_safe = \
        current != next and \
        abs(current - next) <= 3
    
    return is_safe

def is_level_increasing_or_decreasing(report, unsafe_allowance, unsafe_level_count):
    print('\t order: ', report)
    is_increasing = report[0] < report[1]
    i = 0

    while i < len(report):
        if i == len(report) - 1: break
        print('\t\t comparing', report[i], report[i + 1])
        if (report[i] < report[i + 1]) != is_increasing:
            unsafe_level_count += 1
            report.remove(report[i + 1])
        else:
            i += 1
    return unsafe_level_count


def are_level_differences_within_range(report, unsafe_allowance, unsafe_level_count):
    print('\t diff: ', report)
    i = 0
    while i < len(report):
        if i == len(report) - 1: break
        print('\t\t comparing', report[i], report[i + 1])
        if not is_level_safe(report[i], report[i + 1]):
            unsafe_level_count += 1
            report.remove(report[i + 1])
        else:
            i += 1

    return unsafe_level_count


def is_report_safe(report, unsafe_allowance = 0):
    unsafe_level_count = 0
    print(report)
    unsafe_order_level_count = is_level_increasing_or_decreasing(report, unsafe_allowance, unsafe_level_count)
    unsafe_diff_level_count = are_level_differences_within_range(report, unsafe_allowance, unsafe_level_count)

    is_safe = (unsafe_diff_level_count + unsafe_order_level_count) <= unsafe_allowance 

    print(is_safe, unsafe_diff_level_count, unsafe_order_level_count)

    return is_safe


def part_one():
    safe_report_count = 0
    for lines in input:
        report = list(map(lambda n: int(n), lines[0].split(' ')))
        if is_report_safe(report, 0): safe_report_count += 1

    return safe_report_count


def part_two():
    safe_report_count = 0
    for lines in input:
        report = list(map(lambda n: int(n), lines[0].split(' ')))
        if is_report_safe(report, 1): safe_report_count += 1

    print('part two:', safe_report_count)

    return safe_report_count


if __name__ == '__main__':
    # print(part_one())
    # print(part_two())
    part_two()