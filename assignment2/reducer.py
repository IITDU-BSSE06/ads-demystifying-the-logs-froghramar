#!/usr/bin/python

import sys

checker_path = '/assets/js/the-associates.js'
cnt = 0

for line in sys.stdin:
	path = line.strip()
	if path == checker_path:
		cnt = cnt + 1

print cnt

