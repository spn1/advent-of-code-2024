import csv

left = []
right = []

with open('./input.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        numbers = row[0].split('   ')
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))



left.sort()
right.sort()


def part_one():
    diffs = []
    for i in range(len(left)):
        diffs.append(
            abs(
                left[i] - right[i]
            )   
        )
    return sum(diffs)


def part_two():
    products = []
    product_cache = {}
    for i in range(len(left)):
        n = left[i]
        product = product_cache[n] if product_cache.get(n) else n * right.count(n)
        products.append(product)
        if not product_cache.get(n): product_cache[n] = product

    return sum(products)


if __name__ == '__main__':
    print(part_one())
    print(part_two())