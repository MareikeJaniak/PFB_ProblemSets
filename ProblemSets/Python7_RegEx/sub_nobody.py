#!/usr/bin/env python3
import re

with open('./Python_07_nobody.txt', 'r') as text, open('./Michael.txt', 'w') as new:
	contents = text.read()
	
	new.write(re.sub(r"Nobody","Michael",contents))

print("Wrote to file 'Michael.txt'")
	
