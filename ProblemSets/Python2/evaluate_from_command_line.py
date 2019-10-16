#!/usr/bin/env python3

import sys #import sys library to be able to read in variable from command line

count = sys.argv[1]  
count = float(count)     #convert input variable from string to float

if count > 0:
	if count < 50:
		if count % 2 == 0:
			print(count, 'is an even number that is smaller than 50')
		else:
			print(count, 'is an odd number that is smaller than 50')
	elif count > 50:
		if count % 3 == 0:
			print(count, 'is larger than 50 and divisible by 3')
		else:
			print(count, 'is larger than 50 but not divisible by 3')
	else:
		print(count, 'must be equal to 50')
elif count < 0:
	print(count, 'is negative')
elif count == 0:
	print(count, 'is equal to 0')
