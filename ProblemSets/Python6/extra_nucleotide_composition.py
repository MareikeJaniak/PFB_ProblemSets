#!/usr/bin/env python3

nt_count = {}

with open('./Python_06.seq.txt') as seq:
	for line in seq:
		line = line.rstrip()
		seqName,sequence = line.split('\t')
		dna_set = set(sequence)
		G_count = sequence.count('G')                        #count number of Gs in string
		C_count = sequence.count('C')                        #count number of Cs in string
		length = len(sequence)                                                       #determine length of string
		GC_content = ((int(G_count) + int(C_count)) / length) * 100             #add count of Gs and count of Cs, divide by length, and multiply by 100 to get percentage of GC content
		for nt in dna_set:
			count = sequence.count(nt)
			nt_count[nt] = count
		string = 'Gene: {}\n\tAs: {}\n\tCs: {}\n\tGs: {}\n\tTs: {}\n\tGC content: {}\n'
		print(string.format(seqName,nt_count['A'],nt_count['C'],nt_count['G'],nt_count['T'],GC_content))
