"""============================================================================
Project Euler 20

Find the sum of the digits in 100!
============================================================================"""

import tmath as t

def	main():
	total = 0
	digits = str(t.factorial(100))
	for i in digits:
		total += int(i)
	return total
