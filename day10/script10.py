import re
import copy


def read_lines(datafile):
    with open(datafile, 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def check_pair(bins={}, pair=None):
    for key in bins.keys():
        if sorted(pair) == sorted(bins[key]):
            print key


class BinManager:
    def __init__(self, bins):
        self.bins = bins

    def full(self, bot):
        if len(self.bins[bot]) == 2:
            return True
        else:
            return False

    def add_value(self, bot, value):
        if not self.full(bot):
            self.bins[bot].append(value)

    def give_value(self, bots=[]):
        if self.full(bots[0]):
            self.add_value(bots[1], min(self.bins[bots[0]]))
            self.add_value(bots[2], max(self.bins[bots[0]]))
            self.bins[bots[0]] = []


def robot_process(directions, pair=[0, 0]):
    all_bots = {bot[0]: [] for bot in set(re.findall(r'((bot|output) \d+)',
                                                     ''.join(directions)))}
    manager = BinManager(all_bots)
    executed = []
    while len(executed) < len(directions):
        for i, direction in enumerate(directions):
            old = copy.deepcopy(manager.bins)
            if i not in executed:

                if direction.startswith('value'):
                    bot = re.search(r'(bot \d+)', direction).group(1)
                    value = int(re.search(r'value (\d+)', direction).group(1))
                    manager.add_value(bot, value)
                    new = manager.bins

                if direction.startswith('bot'):
                    bots = [b[0] for b in re.findall(r'((bot|output) \d+)',
                                                     direction)]
                    manager.give_value(bots)
                    new = manager.bins

            if old != new:
                executed.append(i)

            if pair:
                check_pair(manager.bins, pair)

            else:
                continue
    return manager.bins


def output_product(bins):
    num = []
    for i in xrange(3):
        num.extend(bins['output ' + str(i)])
    print num[0] * num[1] * num[2]


def main():
    # Parts 1 and 2
    output_product(robot_process(read_lines('input10.txt'), [61, 17]))


if __name__ == '__main__':
    main()
