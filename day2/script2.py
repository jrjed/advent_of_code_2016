def read_instructions(datafile):
    f = open(datafile, 'r+')
    instructions = [line.strip() for line in f]
    f.close()
    return instructions


def kpad(padnum):
    if padnum == 1:
        pad = '''
       .....
       .123.
       .456.
       .789.
       .....
       '''.split()
    elif padnum == 2:
        pad = '''
        .......
        ...1...
        ..234..
        .56789.
        ..ABC..
        ...D...
        .......
        '''.split()
    return pad


def decode(instructions, knum, xi, yi):
    bad = '.'
    keypad = kpad(knum)
    for line in instructions:
        for command in line:
            if command.upper() == 'U' and keypad[yi-1][xi] is not bad:
                yi -= 1
            if command.upper() == 'D' and keypad[yi+1][xi] is not bad:
                yi += 1
            if command.upper() == 'R' and keypad[yi][xi+1] is not bad:
                xi += 1
            if command.upper() == 'L' and keypad[yi][xi-1] is not bad:
                xi -= 1
        print keypad[yi][xi],
    print ''


def main():
    # instructions = ['ull','rrddd','lurdl','uuuud']
    instructions = read_instructions('input2.txt')
    # Part 1
    decode(instructions, 1, xi=2, yi=2)
    # Part 2
    decode(instructions, 2, xi=1, yi=3)


if __name__ == '__main__':
    main()
