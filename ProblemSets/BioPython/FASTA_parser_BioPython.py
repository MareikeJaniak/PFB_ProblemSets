#!/usr/bin/env python3

import Bio
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import GC

seq_list = []
nuc_count = 0
GC_values = []

for seq_record in SeqIO.parse('./Python_08.fasta', 'fasta'):
	seq_list.append(seq_record.seq)
	nuc_count += len(seq_record)
	GC_values.append(GC(seq_record.seq))


num_sequences = len(seq_list)
average_GC = sum(GC_values) / len(GC_values)











print('sequence count:',num_sequences)
print('total number of nucleotides:',nuc_count)
print('average length:',nuc_count/num_sequences)
print('shortest sequence length:',len(min(seq_list)))
print('average GC content:',average_GC)
print('lowest GC content:',min(GC_values))
print('highest GC content:',max(GC_values))
