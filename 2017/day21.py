# solution by sciyoshi
#
# This is a very cool solution.
# He uses numpy arrays to store patterns as booleans.
# Numpy has fast operations for fliplr() and rot90(), which can be combined
# to cover all possible pattern flips and rotations.
# He uses a dictionary to store rules, and very cleverly, uses tobytes() like a
# hash function on 2D numpy arrays, for the keys.
# His code for handling the enhanced grids is very elegant too.
# I didn't know about the // operator, which is floor division producing an int - very handy

import numpy as np

LINES = [l.strip('\n') for l in open('day21_input.txt')]

replacements = {}
for l in LINES:
    src, repl = l.split(' => ')

    src = np.array([[c == '#' for c in b] for b in src.split('/')])
    repl = np.array([[c == '#' for c in b] for b in repl.split('/')])

    flip = np.fliplr(src)

    for i in range(4):
        replacements[src.tobytes()] = repl
        replacements[flip.tobytes()] = repl
        src, flip = np.rot90(src), np.rot90(flip)


pat = np.array([
    [False, True, False],
    [False, False, True],
    [True, True, True],
])

size = 3

# or 5 for part 1
for k in range(18):
    if size % 2 == 0:
        newsize = size // 2 * 3
        newpattern = np.empty((newsize, newsize), dtype=bool)
        for i in range(0, size, 2):
            for j in range(0, size, 2):
                newpattern[i//2*3:i//2*3+3,j//2*3:j//2*3+3] = replacements[pat[i:i+2, j:j+2].tobytes()]
    else:
        newsize = size // 3 * 4
        newpattern = np.empty((newsize, newsize), dtype=bool)
        for i in range(0, size, 3):
            for j in range(0, size, 3):
                newpattern[i//3*4:i//3*4+4,j//3*4:j//3*4+4] = replacements[pat[i:i+3, j:j+3].tobytes()]
    pat = newpattern
    size = newsize
    print('{} : {}'.format(k+1,sum(sum(pat))))