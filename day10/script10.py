import re


def read_lines(datafile):
    with open(datafile, 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def full(pockets):
    if len(pockets) == 2:
        return True
    else:
        return False


def check_pair():
    pass

def robot_process(directions):
    executed = []
    bins = {}
    # add while loop here to keep running over list of directions
    for i, direction in enumerate(directions):
        bot = re.search(r'(bot \d+)', direction).group(1)
        if i not in executed:
            if bot not in bins.keys():
                bins[bot] = [] 

            if direction.startswith('value'):
                value = int(re.search(r'value (\d+)', direction).group(1))
                if not full(bins[bot]):
                    bins[bot].append(value)
                    executed.append(i) # only appending last executed direction?
                    print i

            if direction.startswith('bot') and not full(bins[bot]):
                pass
        else:
            continue
            
    print bins
    print executed
    return bins

robot_process(read_lines('test.txt'))

#bins = robot_process(read_lines('test.txt'))
#print bins
