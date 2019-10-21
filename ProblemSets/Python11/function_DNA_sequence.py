#!/usr/bin/env  python3

#create a DNA sequence class that will contain a sequence, its name, and its organism of origin

class DNA_Sequence(object):
	def __init__(self, sequence, name, organism):
		self.sequence = sequence
		self.name = name
		self.organism = organism

	def get_length(self):
		length = len(self.sequence)
		return length

	def nuc_comp(self):
		dna_set = set(self.sequence)
		nt_count = {}
		for nt in dna_set:
			count = self.sequence.count(nt)
			nt_count[nt] = count
		return nt_count

	def gc_content(self):
		dna = self.sequence
		c_count = dna.count('C')
		g_count = dna.count('G')
		gc_content = (c_count + g_count) / len(dna)
		return gc_content

	def fasta_format(self):
		return('>'+self.name+'\n'+self.sequence)

gene = DNA_Sequence('ATGGACTCATTGGCCAGTC', 'TST1', 'Alouatta palliata')

print(gene.sequence)
print(gene.name)
print(gene.organism)
print('length: {}'.format(gene.get_length()))
print('nucleotide composition: {}'.format(gene.nuc_comp()))
print('GC content: {:.2%}'.format(gene.gc_content()))
print(gene.fasta_format())
