#!/usr/bin/env python3
import sys

input_file = sys.argv[1]

fastaDict = {}

with open(input_file) as fasta_file:
	for line in fasta_file:
		if '>' in line:
			line = line.rstrip()
			gene_id = line.replace('>','')
			fastaDict[gene_id] = ''
		else:
			seq = line.rstrip()
			fastaDict[gene_id] += seq
			
print(fastaDict)			
