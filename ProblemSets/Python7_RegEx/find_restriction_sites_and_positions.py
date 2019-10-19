#!/usr/bin/env python3

import re

with open('./Python_07_ApoI.fasta', 'r') as fasta:
	fasta = fasta.read()
	for (pre, post) in re.findall(r"([AG])(AATT[CT])", fasta):
		print(pre+"^"+post)
