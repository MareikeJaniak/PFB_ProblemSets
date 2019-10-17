#!/usr/bin/env python3
import sys

count = int(sys.argv[1])
num = count

while count > 1:
	num = (num * (count -1))
#	print(num)
	count -= 1
print(num)
print(len(str(num)))
