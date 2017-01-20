import re
import numpy as np


class Screen(object):
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.screen = np.zeros(dimensions).astype('int')

    def rect(self, x, y):
        self.screen[:y, :x] = 1

    def row_rot(self, y, number):
        self.screen[y, :] = np.roll(self.screen[y, :], number)

    def col_rot(self, x, number):
        self.screen[:, x] = np.roll(self.screen[:, x], number)


def directions(datafile):
    with open(datafile) as f:
        contents = f.readlines()
    f.close()
    return contents


def get_args(direction):
    arg1, arg2 = re.search(r'(\d+)(x| by )(\d+)', direction).group(1, 3)
    return int(arg1), int(arg2)


def light_screen(directions, screen_size=(6, 50)):
    s = Screen(screen_size)
    for direction in directions:
        arg1, arg2 = get_args(direction)
        if direction.startswith('rect'):
            s.rect(arg1, arg2)
        elif direction.startswith('rotate row'):
            s.row_rot(arg1, arg2)
        elif direction.startswith('rotate column'):
            s.col_rot(arg1, arg2)
    return s.screen


def print_screen(screen_array):
    for r in screen_array:
        print(''.join([str(n) for n in r]).replace('1', '%')).replace('0', ' ')


def main():
    # Part 1
    print(np.sum(light_screen(directions('input8.txt'))))
    # Part 2
    print_screen(light_screen(directions('input8.txt')))


if __name__ == '__main__':
    main()
