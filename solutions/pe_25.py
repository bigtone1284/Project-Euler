"""============================================================================
Project Euler 25

Find the first Fibonacci number with 1000 or more digits.  
============================================================================"""
import tmath as t

def main():
	gen = t.gen_fibonacci()
	length = 0
	term = 0
	
	while length < 1000:
		term += 1
		temp = gen.next()
		length = len(str(temp))
	return term-1

print main()
