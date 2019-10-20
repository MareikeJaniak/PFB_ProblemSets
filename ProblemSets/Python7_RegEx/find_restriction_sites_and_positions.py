#!/usr/bin/env python3

import re

with open('./Python_07_ApoI.fasta', 'r') as fasta:
	fasta = fasta.read()
	fasta = re.sub(r"[\n]","", fasta)
	for found in re.finditer(r"([AG])(AATT[CT])([A-Z]+?)([AG])(AATT[CT])", fasta):
		whole = found.group(0)
		pre = found.group(1)
		post = found.group(2)
		middle = found.group(3)
		pre2 = found.group(4)
		post2 = found.group(5)
		print(pre+"^"+post+middle+pre2+"^"+post2)
