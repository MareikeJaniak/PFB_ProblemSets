#!/usr/bin/env python3

import re

with open('./Python_07_ApoI.fasta', 'r') as fasta:
	fasta = fasta.read()
	fasta = re.sub(r'\n', '', fasta)
	sites = re.findall(r"[AG]AATT[CT]", fasta)
	print(sites)
