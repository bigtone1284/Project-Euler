"""============================================================================
Project Euler 30

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.
============================================================================"""

def power_digit(n):
	banana = 0
	stringer = str(n)
	for i in stringer:
		banana += int(i)**5
	if banana == n:
		return True
	else:
		return False



	
	
def main():
	total = 0
	for i in range (2,5*9**5):
		if power_digit(i) == True:
			total += i
	return total
