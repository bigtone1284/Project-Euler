"""============================================================================
Project Euler 19

You are given the following information, but you may prefer to do some research
 for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century 
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?
============================================================================"""

def sunday(d,m,y):
	if str(y)[0:2] == "19":
		c = 2
	elif str(y)[0:2] == "20":
		c = 0
	yL2 = int(str(y)[2:])
	
	yCode = (yL2 + (yL2 /4)) % 7
	
	mDict = {1:0,2:3,3:3,4:6,5:1,6:4,7:6,8:2,9:5,10:0,11:3,12:5}
	
	mLDict = {1:6,2:2,3:3,4:6,5:1,6:4,7:6,8:2,9:5,10:0,11:3,12:5}
	
	if y % 4 == 0:
		mCode = mLDict.get(m)
	else:
		mCode = mDict.get(m)
	
	if (d + mCode + yCode + c) % 7 == 2:
		return True
	else:
		return False
		
		# I really don't know why modulo 2.  Best I have is that this century begins on a Tuesday?
		

def main():
	count = 0
	for year in range(1901,2001):
		for month in range (1,13):
			if sunday(1,month,year) == True:
				count += 1
	return count
