#!/usr/bin/env python3
import re
import sys

def wrap_dna(dna, width):
	nt_list = []
	new = ''
	dna = re.sub(r'\n', '', dna)
	width = int(width)
	for nt in dna:
		nt_list.append(nt)
	for index in nt_list:
		new += "".join(nt_list[:width])+'\n'
		del nt_list[:width]
	return new.rstrip() 


fasta = sys.argv[1]
width = int(sys.argv[2])

with open(fasta, 'r') as dna:
	dna = dna.read()
	wrapped = wrap_dna(dna, width)
print(wrapped)
