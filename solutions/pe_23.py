"""============================================================================
Project Euler 23

A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors of 28 
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers is 
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum 
of two abundant numbers.
============================================================================"""
import tmath as t

def abundant_num(n):
	divs = proper_div(n)
	total = 0
	for i in divs:
		total += i
	if total > n:
		return True
	else:
		return False

def proper_div(n):
	return t.factors(n)[:-1]
	
def main():
	abund_nums = []
	ab_hash = {}
	total = 0
	for i in range(12,28130):
		if abundant_num(i) == True:
			abund_nums.append(i)
			ab_hash[i] = i
	for S in range(1, 28130):
		flag = True
		for n in abund_nums:
			if ab_hash.get(S-n) != None:
				flag = False
				break
		if flag: total += S
	return total

print main()
