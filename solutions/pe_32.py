"""============================================================================
Project Euler 32

Find the sum of all product that are part of a pan-digital number sentence.  
============================================================================"""

import tmath as t

def main():
	total = []
	for i in range(1,60):
		for j in range(1,2000):
			z = str(i) + str(j) + str(i*j)
			if t.is_pan_digital(z) == True and len(z) == 9:
				total.append(i*j)
	return sum(set(total))
