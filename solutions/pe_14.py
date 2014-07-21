"""============================================================================
Project Euler 14

A Collatz sequence iterates with the following rules:

n/2 if n is even
3n + 1 if n is odd.

if n = 13
13-40-20-10-5-16-8-4-2-1

What is the longest Collatz Sequence under 1 million?

============================================================================"""

import tmath as t

def get_value(dictionary, search_value):

    for key, value in dictionary.iteritems():
        if value == search_value: return key



def main():

    chains = {}
    m = max(t.collatz_Seq(i, chains) for i in range(1,1000000))
    return get_value(chains, m)
