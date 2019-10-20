#!/usr/bin/env python3

import re

middle_fragments_list = []

with open('./Python_07_ApoI.fasta', 'r') as fasta:
	fasta = fasta.read()
	fasta = re.sub(r"[\n]","", fasta)
	for found in re.finditer(r"([AG])(AATT[CT])([A-Z]+?)([AG])(AATT[CT])", fasta):     # reg ex to find pattern of restriction enzyme cut sites (R^AATTY) with variable sequence in between
		pre = found.group(1)
		post = found.group(2)
		middle = found.group(3)
		pre2 = found.group(4)
		post2 = found.group(5)
		fragments = pre+"^"+post+middle+pre2+"^"+post2        #create string of regex match with ^ to denote cut sites
		fragments_list = fragments.split('^')									# add all fragments of regex match to list, which has three entries: base before cut, middle, and base after next cut
		middle_fragments_list.append(fragments_list[1])				# add middle fragments (in between cut sites) to a new list
gel = sorted(middle_fragments_list, key = len, reverse = True)		# create variable that contains fragments sorted from largest to smallest
print(*gel, sep = '\n')																						# print fragments on their own lines, with largest on top, smallest on bottom - like in gel
