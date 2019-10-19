#!/usr/bin/env python3
import sys
import re

codon_dict = {}

file = ''

try:
	file = sys.argv[1]
	print("User provided file: ", file)
	with open(file, 'r') as fasta:
		for line in fasta:
			if '>' in line:
				line = line.rstrip()
				seq_name = re.sub(r'>','', line)
				codon_dict[seq_name] = ''
				codon_list = []
			else:
				line = line.rstrip()
				codons = re.findall(r"([A-Za-z]{3})",line)
				codon_list.extend(codons)		
				codon_dict[seq_name] = codon_list
except IndexError:
	print('Please provide a file name')
except IOError:
	print("Can't find file: ", file)

with open('./Python_08.codons-frame-1.nt','w') as output:
	for gene in codon_dict:
		print(gene+'-frame-1-codons\n'+" ".join(codon_dict[gene])+'\n')
