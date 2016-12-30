def read_rows(datafile):
    f = open(datafile, 'r+')
    triangles = []
    for line in f:
        triangles.append([int(number) for number in line.split()])
    f.close()
    return triangles


def chunker(datafile, size=3):
    columns = zip(*read_rows(datafile))
    numbers = [i for col in columns for i in col]
    triangles = [numbers[i:i+size] for i in range(0, len(numbers), size)]
    return triangles


def triangle_test(triangle):
    triangle = sorted(triangle)
    return sum(triangle[:2]) > triangle[2]


def triangle_counter(triangles):
    results = [triangle_test(triangle) for triangle in triangles]
    return sum(results)


def main():
    # Part 1
    print(triangle_counter(read_rows('input3.txt')))
    # Part 2
    print(triangle_counter(chunker('input3.txt')))


if __name__ == '__main__':
    main()
