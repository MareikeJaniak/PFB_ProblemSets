#!/usr/bin/env python3

import re

codon_dict = {}

with open('./Python_08.fasta') as fasta:
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

with open('./Python_08.codons-frame-1.nt','w') as output:
	for gene in codon_dict:
		#string = '{}-frame-1-codons\n{}'
		#print(string.format(gene, *codon_dict[gene]))
		#print(*codon_dict[gene])
		#print(" ".join(codon_dict[gene]))
		output.write(gene+'-frame-1-codons\n'+" ".join(codon_dict[gene])+'\n')
