"""============================================================================
Project Euler 07

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10 001st prime number?

Solution:  This is how you find the nth prime.  
============================================================================"""
import tmath as t

	
def main():
	gen = t.gen_Sieve_of_eratosthenes()
	for i in range(10001):
		p = gen.next()
		result = p
	return p
