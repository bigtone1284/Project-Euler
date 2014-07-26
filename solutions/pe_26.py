"""============================================================================
Project Euler 26

Find the fraction 1/n with the longest recurring cycle in decimal fraction.

Recall Fermat's Little Theorem

============================================================================"""
import tmath as t


def main():
	primes = t.primes(1000)
	c = 1
	for p in primes[::-1]:
		while pow(10, c, p) - 1 != 0:
			c += 1
		if (p-c) == 1: break
	
	return p
