"""============================================================================
Project Euler 15

There are 6 routes through a 2 x 2 grid.  How many routes are there in a 20 x
20 grid?

I really need to review this and figure out what a figurate number is.  
============================================================================"""

import tmath as t


def main():
    result = 1
    M = 20
    for n in range(1, M+1):
        result += t.getFigurate(n, M)
    return result

print main()
