#!/usr/bin/env python3

seqs = {}
nt_comp = {}

with open('./Python_08.fasta') as seq:
	for line in seq:
		if '>' in line:
			line = line.rstrip()
			gene_id = line.replace('>','')
			seqs[gene_id] = {'nt_comp' : {}} #{ 'nt_comp' : {}}})
		else:
			sequence = line.rstrip()
			dna = set(sequence)
			for nt in dna:
				if nt not in seqs[gene_id]['nt_comp']:
					seqs[gene_id]['nt_comp'][nt] = 0
				else:
					count = sequence.count(nt)
					seqs[gene_id]['nt_comp'][nt] += count
print(seqs)

#fastaDict[gene_id] += seq
