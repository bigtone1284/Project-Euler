"""============================================================================
Project Euler 21

if d(n) = factors of n  (except n), then numbers a and b are amicable numbers 
if:

a(n) = b AND b(n) = a and b != a

============================================================================"""

import tmath as t

def factors_n(n):
	total = 0
	for i in t.factors(n)[:-1]:
		total += i
	return total

def	main():
	sums = []
	total_sum = 0
	for a in range (10000):
		sums.append(factors_n(a))
	
	for i in range(len(sums)):
		if i == factors_n(sums[i]) and sums[i] == factors_n(i) and sums[i] != i:
			total_sum += i
	return total_sum
