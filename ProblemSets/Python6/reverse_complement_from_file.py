#!/usr/bin/env python3

with open("./Python_06.seq.txt", 'r') as seq:
	for line in seq:
		seqName, sequence = line.split('\t')
		seq_complement = sequence.replace('A', 't').replace('C','g').replace('T','A').replace('G','C')    #replace each letter with complement, but make first two lower case to avoid replacing initial replacements
		seq_complement_upper = seq_complement.upper()                 #return everything to upper case
		seq_reverse_complement = seq_complement_upper[::-1]             #reverse the sequence

		string = '>{}_reverse_complement{}'
		print(string.format(seqName,seq_reverse_complement))
