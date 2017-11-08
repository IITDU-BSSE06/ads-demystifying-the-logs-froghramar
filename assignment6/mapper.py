#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		ip, hp1, hp2, dateTime, gmt, req, path, req_type, status, val = data
		splited_array = dateTime.split("/")
		date = splited_array[2]
		year = date.split(":")[0]
		print "{0}".format(year)


