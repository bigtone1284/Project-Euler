"""============================================================================
Project Euler 34

digit factorials
============================================================================"""
import math
def main():
	
	def digit_factorials (x):
		total = 0
		for i in str(x):
			total += math.factorial(int(i))
		
		return total
	
	add = 0
	for i in range(3,100000):
		if i == digit_factorials(i):
			add += i
	return add
