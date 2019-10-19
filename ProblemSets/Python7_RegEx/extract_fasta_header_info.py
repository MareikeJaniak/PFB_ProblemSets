#!/usr/bin/env python3

import re

with open('./Python_07.fasta') as fasta:
	fasta = fasta.read()
	for (gene_id, description) in re.findall(r">(\S+) (.+)", fasta):
		print("id: ",gene_id, "desc: ",description)
