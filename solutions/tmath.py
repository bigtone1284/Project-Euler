"""============================================================================

These are some functions I've written/borrowed/stolen (with attribution) for 
helping me solve Project Euler Math Problems.  

I was recommended this assignment from Greg Gundersen.
============================================================================"""
import math
 


def gen_Sieve_of_eratosthenes():
    """ Generate an infinite sequence of prime numbers.
    
    # Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
    
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1


def nthFibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return nthFibonacci(n-1) + nthFibonacci(n-2)

def seqFibonacci():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b



		
