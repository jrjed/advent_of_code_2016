import re
import numpy as np
import collections

def directions(datafile):
    with open(datafile) as f:
        contents = f.read().split('\n')
    f.close()
    return contents

class Screen(object):
    '''
    Dimensions should be given (y, x)
    '''
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.screen = np.zeros(dimensions)

    def rect(self, subdim):
        self.screen[:subdim[0],:subdim[1]] = 1

    def row_rot(self, y, intervals):
        row = collections.deque(self.
        

def delegate(direction):
    pass
