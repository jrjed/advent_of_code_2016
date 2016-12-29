def read_directions(datafile):
    f = open(datafile, 'r+')
    steps = [step.strip() for step in f.read().split(',')]
    f.close()
    return steps


def checkpoints(steps):
    # dpad = [North, East, South, West]
    dpad = [0, 0, 0, 0]
    dselect = 0
    positions = [(0, 0)]
    for step in steps:
        dir, count = step[0], int(step[1:])
        if dir.upper() == 'R':
            dselect += 1
        else:
            dselect -= 1

        if dselect > 3:
            dselect -= 4
        elif dselect < -4:
            dselect += 4

        dpad[dselect] += count
        positions.append((dpad[1] - dpad[3], dpad[0] - dpad[2]))
    return positions


def trace_path(positions):
    # Can probably be done much more concisely and elegantly
    all_positions = []
    for i in xrange(len(positions)-1):
        if positions[i+1][0] != positions[i][0] and positions[i+1][0] > positions[i][0]:
            path = [(j, positions[i+1][1]) for j in xrange(positions[i][0], positions[i+1][0])]
        elif positions[i+1][0] != positions[i][0] and positions[i+1][0] < positions[i][0]:
            path = [(j, positions[i+1][1]) for j in xrange(positions[i][0], positions[i+1][0], -1)]
        elif positions[i+1][1] != positions[i][1] and positions[i+1][1] > positions[i][1]:
            path = [(positions[i+1][0], j) for j in xrange(positions[i][1], positions[i+1][1])]
        elif positions[i+1][1] != positions[i][1] and positions[i+1][1] < positions[i][1]:
            path = [(positions[i+1][0], j) for j in xrange(positions[i][1], positions[i+1][1], -1)]
        all_positions.extend(path)
    all_positions.append(positions[-1])
    return all_positions


def first_twice_visited(all_positions):
    for i, position in enumerate(all_positions[1:]):
        if position not in all_positions[:i]:
            continue
        else:
            return all_positions[i+1]


def distance(final_position):
    print('{} block(s)'.format(sum([abs(i) for i in final_position])))


def main():
    # Part 1
    distance(checkpoints(read_directions('input1.txt'))[-1])
    # Part 2
    distance(first_twice_visited(trace_path(checkpoints(read_directions('input1.txt')))))


if __name__ == '__main__':
    main()
