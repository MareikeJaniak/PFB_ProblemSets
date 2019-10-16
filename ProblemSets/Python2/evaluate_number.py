#!/usr/bin/env python3

count = 50

if count > 0:
	#print(count, 'is positive')
	if count < 50:
		#print(count, 'is smaller than 50')
		if count % 2 == 0:
			print(count, 'is an even number that is smaller than 50')
	elif count > 50:
		if count % 3 == 0:
			print(count, 'is larger than 50 and divisible by 3')
	else:
		print(count, 'must be equal to 50')
elif count < 0:
	print(count, 'is negative')
elif count == 0:
	print(count, 'is equal to 0')
