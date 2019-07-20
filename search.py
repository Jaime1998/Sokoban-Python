#!/usr/bin/python
# -*- coding: utf-8 -*-
from state import *

if __name__ == '__main__':
    obstacles = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (1,0), (1,4), (1,5), (2,0), (2,5), (3,0), (3,5), (4,0), (4,5), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5)]
    storages = {(2,1): 0, (2,3):1}
    stateObj = State((1,2), {(2,2):0, (2,3):1})
    stateObj.possibleMoves(storages, obstacles)
    