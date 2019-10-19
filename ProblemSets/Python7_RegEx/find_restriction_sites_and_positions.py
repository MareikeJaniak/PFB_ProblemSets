#!/usr/bin/env python3

import re

with open('./Python_07_ApoI.fasta', 'r') as fasta:
	fasta = fasta.read()
	fasta = re.sub(r"[\n]","", fasta)
	for (pre, post, middle, pre2, post2) in re.findall(r"([AG])(AATT[CT])([A-Z]+)([AG])(AATT[CT])", fasta):
		print(pre+"^"+post+pre2+"^"+post2)
