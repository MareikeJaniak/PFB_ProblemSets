#!/usr/bin/env python3

import sys
import re

def rev_comp(dna):
	dna = re.sub(r'\n', '', dna)
	dna = dna.rstrip('\n')
	seq_complement = dna.replace('A', 't').replace('C','g').replace('T','A').replace('G','C')    #replace each letter with complement, but make first two lower case to avoid replacing initial replacements
	seq_complement_upper = seq_complement.upper()                 #return everything to upper case
	seq_reverse_complement = seq_complement_upper[::-1]             #reverse the sequence
	return seq_reverse_complement

file = sys.argv[1]

with open(file, 'r') as dna:
	dna = dna.read()

print(rev_comp(dna))
