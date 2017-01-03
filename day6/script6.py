import collections


def readcol(datafile):
    with open(datafile) as f:
        rows = []
        for line in f:
            rows.extend(line.split())
        columns = zip(*[list(row) for row in rows])
    f.close()
    return columns


def decode_col(columns, rank):
    code = ''
    for column in columns:
        count = collections.Counter(column)
        if rank.lower() == 'most':
            sel = 0
        else:
            sel = len(count) - 1
        letter = count.most_common()[sel][0]
        code += letter
    return code


def main():
    # Part 1
    print(decode_col(readcol('input6.txt'), 'most'))
    # Part 2
    print(decode_col(readcol('input6.txt'), 'least'))


if __name__ == '__main__':
    main()
