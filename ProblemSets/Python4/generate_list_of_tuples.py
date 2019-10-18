#!/usr/bin/env python3

seq_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

tup_list = []
tup = ()
for seq in seq_list:
	tup = len(seq),seq
	tup_list.append(tup)

print(tup_list)
