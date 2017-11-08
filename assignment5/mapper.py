#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		ip, hp1, hp2, date, gmt, req, path, req_type, status, val = data
		print "{0}".format(path)


