#!/usr/bin/env python3

nums = [101,2,15,22,95,33,2,27,72,15,52]
even_sum = 0
odd_sum = 0

for num in nums:
	print(num)
	if num % 2 == 0:
		even_sum += num
	else:
		odd_sum += num
string = 'Sum of even numbers:{}\nSum of odd:{}'

print(string.format(even_sum, odd_sum))
