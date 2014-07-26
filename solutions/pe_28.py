"""============================================================================
Project Euler 28

Find the sum of the diagnols in a 1001x1001 spiral square.  
============================================================================"""
import tmath as t
def main():
	total = 1
	for i in range(2,1002):
		if t.isOdd(i) == True:
			total += 4*(i**2)-6*(i-1)
	return total
