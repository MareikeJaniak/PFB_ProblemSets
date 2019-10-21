#!/usr/bin/env  python3

#create a DNA sequence class that will contain a sequence, its name, and its organism of origin

class DNA_Sequence(object):
	def __init__(self, sequence, name, organism):
		self.sequence = sequence
		self.name = name
		self.organism = organism



gene = DNA_Sequence('ATGGACTCATTGGCCAGTC', 'TST1', 'Alouatta palliata')

print(gene.sequence)
print(gene.name)
print(gene.organism)
