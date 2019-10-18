#!/usr/bin/env python3

import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

nums = list(range(start,end+1))

for num in nums:
	if num % 2 != 0:
		print(num)
