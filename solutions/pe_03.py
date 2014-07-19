"""============================================================================
Project Euler 03

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Solution:  I began to learn about sieves here.  Sieves of primes are algorithms 
for finding primes that run better than more basic methods algorithms that try 
to find primes, usually by going int by int through a range and checking its
"%" versus all previous ints.  



============================================================================"""
import tmath as t

def main():
	
	result = 0
	n = 600851475143
	limit = int(n**0.5)
	gen = t.gen_Sieve_of_eratosthenes()
	p = gen.next()
	
	while p < limit:
		if n % p == 0:
			prime = p
		p = gen.next()
	return prime
