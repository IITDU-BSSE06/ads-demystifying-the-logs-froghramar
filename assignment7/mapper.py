#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		ip, hp1, hp2, dateTime, gmt, req, path, req_type, status, val = data
		formatted_req = req[1:]
		print "{0}".format(formatted_req)


