#!/usr/bin/env python3
import sys
import re

input_file = sys.argv[1]

fastaDict = {}

with open(input_file) as fasta_file:	
	fasta_file = fasta_file.read()
	for (gene_id, sequence) in re.findall(r">(\S+) .*\n([A-Za-z\n]+)",fasta_file):
		sequence = re.sub(r"[\n]",'', sequence)
		fastaDict[gene_id] = sequence

print(fastaDict)
