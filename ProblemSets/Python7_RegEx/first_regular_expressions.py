#!/usr/bin/env python3
import re

with open('./Python_07_nobody.txt', 'r') as text:
	contents = text.read()

for found in re.finditer(r"Nobody", contents):
	print(found.start(0)+1)


