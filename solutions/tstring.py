"""============================================================================
These are some functions I've written/borrowed/stolen (with attribution) for 
helping me deal with strings.  

I was recommended this assignment from Greg Gundersen.
============================================================================"""
def is_palindrome(n):
	if " " in str(n):
		n = n.replace(" ","") 
	if str(n).lower() == str(n)[::-1].lower():
 		return True
 	else:
 		return False
 		
def int_to_str(n):
	return str(n)
