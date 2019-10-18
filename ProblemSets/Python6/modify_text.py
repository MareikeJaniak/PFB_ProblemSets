#!/usr/bin/env python3

with open("./Python_06.txt", 'r') as text_read, open("./Python_06_uc.txt", 'w') as text_print:
	for line in text_read:
		text_print.write(line.upper() + "\n")

print("Wrote upper case text to file 'Python_06_uc.txt'")
