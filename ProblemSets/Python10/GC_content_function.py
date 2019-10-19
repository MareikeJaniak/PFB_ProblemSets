#!/usr/bin/env python3
import sys

def gc_content(dna):
	c_count = dna.count('C')
	g_count = dna.count('G')
	gc_content = (c_count + g_count) / len(dna)
	return gc_content

file = sys.argv[1]

with open(file, 'r') as dna:
	dna = dna.read()

gc_cont = gc_content(dna)
perc_gc = '{:.2%}'.format(gc_cont)
print('The GC content of the sequence is:',perc_gc) 
