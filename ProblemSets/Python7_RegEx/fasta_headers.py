#!/usr/bin/env python3

import re

with open('./Python_07.fasta') as fasta:
	fasta = fasta.read()
#	print(fasta)
	headers = re.findall(r">\S+ .+", fasta)
	print(headers)
