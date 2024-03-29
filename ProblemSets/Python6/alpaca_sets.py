#!/usr/bin/env python3

all_genes_set = set()
stemcell_set = set()
pigmentation_set = set()
transcription_set = set()

with open('./alpaca_all_genes.tsv', 'r') as all_genes:
	for line in all_genes:
		if 'Gene' not in line:
			line = line.rstrip()
			gene_id,gene_stable,gene_transcript = line.split('\t')
			all_genes_set.add(gene_id)

with open('./alpaca_stemcellproliferation_genes.tsv','r') as stemcell_genes:
	for line in stemcell_genes:
		if 'Gene' not in line:
			line = line.rstrip()
			gene_id,gene_stable,gene_transcript = line.split('\t')
			stemcell_set.add(gene_id)

with open('./alpaca_pigmentation_genes.tsv','r') as pig_genes:
	for line in pig_genes:
		if 'Gene' not in line:
			line = line.rstrip()
			gene_id,gene_stable,gene_transcript = line.split('\t')
			pigmentation_set.add(gene_id)

with open('./alpaca_transcriptionFactors.tsv','r') as transcription_factors:
	for line in transcription_factors:
		if 'Gene' not in line:
			line = line.rstrip()
			gene_id,gene_stable,gene_transcript = line.split('\t')
			transcription_set.add(gene_id)

#print(all_genes_set - stemcell_set)
print('Genes that are both stemcell proliferation genes and pigment genes:',stemcell_set & pigmentation_set)
print('Genes that are transcription factors for cell proliferation:',transcription_set & stemcell_set)
