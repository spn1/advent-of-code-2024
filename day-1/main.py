import csv

left = []
right = []
diffs = []

with open('./input.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        numbers = row[0].split('   ')
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))


def main():
    left.sort()
    right.sort()

    for i in range(len(left)):
        diffs.append(
            abs(
                left[i] - right[i]
            )
        )

    print(diffs)
    print(sum(diffs))


if __name__ == '__main__':
    main()