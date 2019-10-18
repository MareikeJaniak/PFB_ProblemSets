#!/usr/bin/env python3

seq_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for seq in seq_list:
	print(seq)

for seq in seq_list:
	string = '{}\t{}'
	print(string.format(len(seq),seq))
