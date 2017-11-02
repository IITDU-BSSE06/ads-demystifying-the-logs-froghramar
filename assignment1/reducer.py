#!/usr/bin/python

import sys

checker_ip = '10.99.99.186'
cnt = 0

for line in sys.stdin:
	ip = line.strip()
	if ip == checker_ip:
		cnt = cnt + 1

print cnt

