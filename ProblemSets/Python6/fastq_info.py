#!/usr/bin/env python3

line_count = 0
character_count = 0
total_length = 0

with open('./Python_06.fastq', 'r') as fastq:
	for line in fastq:
		line_count += 1
		total_length += len(line)
		for character in line:
			character_count += 1

average_length = total_length / line_count
print('Total number of lines:',line_count)
print('Total number of characters:',character_count)
print('Average line length:',average_length)
