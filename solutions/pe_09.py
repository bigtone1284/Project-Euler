"""============================================================================
Project Euler 09

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Solution:  I made a function to find pythogorean triples, so I looped through 
the two smaller pieces of a pythogorean triple, and used my function to find c.  

============================================================================"""
import tmath as t

sum = 1000
limit = (sum/2)


def main():
	for i in range(limit):
		for j in range(limit):
			if i + j + t.pythogorean(i,j) == sum and i != j:
				return int(i*j*t.pythogorean(i,j))
