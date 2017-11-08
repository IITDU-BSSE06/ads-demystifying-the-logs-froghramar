#!/usr/bin/python

import sys
from urlparse import urlparse

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		ip, hp1, hp2, date, gmt, req, path, req_type, status, val = data
		relative_path = urlparse(path).path
		print "{0}".format(relative_path)


