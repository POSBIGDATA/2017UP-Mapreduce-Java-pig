#!/usr/bin/python3
import sys
import re

for line in sys.stdin:
	line = re.sub(re.compile('([^A-Z a-z])+'), ' ', line)
	words = line.strip().split()
	for word in words:
		print (word.upper() + '\t1')
