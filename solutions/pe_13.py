"""============================================================================
Project Euler 13

Work out the first ten digits of the sum of the following one-hundred 50-digit 
numbers.

...moved to pe_13_txt.txt

Solution:  pretty straight forward but learning how to use path and os.  

Used solution from Greg Gundersen.  
============================================================================"""

import os


def main():
    
    result = 0
    path = os.path.normpath(os.path.dirname(__file__) +
        'pe_13_txt.txt')

    with open(path) as f:
        lines = f.readlines()
    f.close()

    for l in lines:
        result += int(l)
    return int(str(result)[:10])
