"""============================================================================

These are some functions I've written/borrowed/stolen (with attribution) for 
helping me solve Project Euler Math Problems.  

I was recommended this assignment from Greg Gundersen.
============================================================================"""

def seqFibonacci():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b

def nthFibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return nthFibonacci(n-1) + nthFibonacci(n-2)

