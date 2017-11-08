#!/usr/bin/python

import sys

counter = dict()

requests = ["HEAD", "GET", "PROPFIND", "PUT", "POST", "OPTIONS", "DELETE"]

for line in sys.stdin:
	req = line.strip()
	if req in requests:
		counter[req] = counter.get(req, 0) + 1

for req in counter:
	print "{0}\t{1}".format(req, counter.get(req, 0))

