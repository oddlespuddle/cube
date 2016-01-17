#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pykociemba import search
from time import time
from turn import TurnSequence

errors = {
    'Error 1': 'There is not exactly one facelet of each colour',
    'Error 2': 'Not all 12 edges exist exactly once',
    'Error 3': 'Flip error: One edge has to be flipped',
    'Error 4': 'Not all corners exist exactly once',
    'Error 5': 'Twist error: One corner has to be twisted',
    'Error 6': 'Parity error: Two corners or two edges have to be exchanged',
    'Error 7': 'No solution exists for the given maxDepth',
    'Error 8': 'Timeout, no solution within given time'
}

def solve(facelets, maxDepth = 24, timeOut = 1000, useSeparator = False):
    t = time()
    res = search.Search().solution(facelets, maxDepth, timeOut, useSeparator).strip()
    if res in errors:
        return res, time() - t, errors[res]
    else:
        return TurnSequence(res), time() - t

def solve_optimal(facelets, verbose = False):
    moves = 0
    t = time()
    while True:
        if verbose:
            print('Minimum Moves Calculating: %d, Time: %.2f' % (moves, time() - t))
        ret = solve(facelets, moves, timeOut = -1)
        if ret[0] == 'Error 7':
            moves += 1
        elif not type(ret[0]) == TurnSequence:
            return ret
        else:
            return ret



if __name__=='__main__':
    if len(sys.argv) > 1:
        print(solve(sys.argv[1]))
    else:
        while True:
            try:
                print(solve(input()))
            except:
                print('Usage: kociemba <cubestring>\nfor example:\nkociemba DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')

