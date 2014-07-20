"""============================================================================
Project Euler 05

2520 is the smallest number that can be divided by each of the numbers from 1 
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

Solution:

learned how to execute divide_by_array(n).  Also, just check 11-20 because all
of those numbers are divisible by 1-20.  

============================================================================"""

import tmath as t

def divide_by_array(n):
	for i in test_array:
		if n % i != 0:
			return False
	return True

def main():
	test_array = [11,12,13,14,15,16,17,18,19,20]
	n = 2520
	i = 2520
	while t.divide_by_array(n, test_array) == False:
		n += i
	return n
