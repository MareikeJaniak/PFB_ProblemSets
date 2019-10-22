#!/usr/bin/env python3

import sys

program = sys.argv[1]
search_strat = sys.argv[2]
scoring_matrix = sys.argv[3:]

#file = './blast_'+search_strat+'_v_qfo_'+scoring_matrix+'.txt'

field_names = ['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits']
result_dict = {}

for matrix in scoring_matrix:
	with open('./'+program+'_'+search_strat+'_v_qfo_'+matrix+'.txt', 'r') as result_file:
		for line in result_file:
			if line[0]!='#':
				line = line.rstrip()
				result_fields = line.split('\t')
				matrix_dict = dict(zip(field_names, result_fields))
				result_dict[matrix] = matrix_dict
				break			

#print(result_dict)

print('matrix  ','% ident','al_len','evalue',sep='\t')
for matrix in scoring_matrix:
	print(matrix,result_dict[matrix]['percid'],result_dict[matrix]['alen'],result_dict[matrix]['evalue'], sep='\t')
