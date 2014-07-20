"""============================================================================
Project Euler 04

A palindromic number reads the same both ways.  The largest palindrome made
from two 2-digit numbers is 9009 = 91 * 99.  

Find the largest palindrome made from the product of two 3-digit numbers.

Solution:  Iterate over range 1000 to find palindromes and test using 
is_palindrome().  Then find max value of the palindromes.  



============================================================================"""

import tstring


def main():
	palindromes = []
	result = 0
	for i in range (1000):
		for j in range(1000):
			if tstring.is_palindrome(i*j) == True:
				palindromes.append(i*j)
	return max(palindromes)

	
