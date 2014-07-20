"""============================================================================
Project Euler 06

The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... +
10^2 = 385.

The square of the sums of the first natural numbers is (1 + 2 + ... + 10)^2 = 
3025.  

Their difference is 2640.

Find the same difference for the first 100 natural numbers.

============================================================================"""


def main():
	sum = 0
	sum_of_squares = 0
	for i in range(101):
		sum += i
		sum_of_squares += i**2
	return sum**2 - sum_of_squares
