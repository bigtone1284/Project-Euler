"""============================================================================
Project Euler 22

There is a txt tile with thousands of names.  

Each name has a name score of its letters' combined point value:

COLIN = 3 + 15 + 12 + 9 + 11 = 53

This plus the nth listing in the txt file (COLIN is 938) = the score for Colin.  

Find the total score of all names together.  

============================================================================"""
alpha_dict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
import ast

def name_score(n):
	score = 0
	for i in n:
		score += alpha_dict.get(i)
	return score
 
def get_names():
	with open('pe_22_names.txt') as f:
  		names = sorted(ast.literal_eval(f.read()))
	return names
	
def main():
	n = get_names()
	total = 0
	for i in n:
		total += (name_score(i) * (1 + n.index(i)))
	return total
