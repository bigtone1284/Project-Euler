"""============================================================================
Project Euler 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
============================================================================"""

import tmath as t

def main():
	result = 0	
	n = 2000000
	gen = t.gen_Sieve_of_eratosthenes()
	p = gen.next()
	
	while p < n:
		result += p
		p = gen.next()
	return result
	
print main()
