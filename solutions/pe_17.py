"""============================================================================
Project Euler 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 
342 (three hundred and forty-two) contains 23 letters and 
115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.

Probably could have solved this more cleanly....
============================================================================"""



def main():
	word = 0
	num_map = {
        '0' : ['',''],
        '1' : ['one', 'one'],
        '2' : ['two','twenty'],
        '3' : ['three', 'thirty'],
        '4' : ['four', 'forty'],
        '5' : ['five', 'fifty'],
        '6' : ['six', 'sixty'],
        '7' : ['seven', 'seventy'],
        '8' : ['eight', 'eighty'],
        '9' : ['nine', 'ninety'],
        '10' : ['ten'],
        '11' : ['eleven'],
        '12' : ['twelve'],
        '13' : ['thirteen'],
        '14' : ['fourteen'],
        '15' : ['fifteen'],
        '16' : ['sixteen'],
        '17' : ['seventeen'],
        '18' : ['eighteen'],
        '19' : ['nineteen'],
        'h' : ['hundredand']
    }
	for i in range (1,1001):
		if i < 10:
			word += len(num_map.get(str(i), None)[0])
		elif str(i) == "1000":
			word += len("onethousand")
		elif i >= 10 and i < 20:
			word += len(num_map.get(str(i), None)[0])
		elif i >= 20 and i < 100:
			word += len(num_map.get(str(i)[1], None)[0]) + len(num_map.get(str(i)[0], None)[1])
		elif i >= 100 and i < 1000:
			if "00" in str(i):
				word += len (num_map.get(str(i)[0], None)[0]) + len("hundred")
			elif str(i)[1] == "0":
				word += len(num_map.get(str(i)[0], None)[0]) + len("hundredand") + len(num_map.get(str(i)[2], None)[0])
			elif str(i)[1] == "1":
				word += len(num_map.get(str(i)[0], None)[0]) + len("hundredand") + len(num_map.get(str(i)[1:], None)[0])
			else:
				word += len(num_map.get(str(i)[0], None)[0]) + len("hundredand") + len(num_map.get(str(i)[1], None)[1]) + len(num_map.get(str(i)[2], None)[0])
	
	return word
print main()
		
