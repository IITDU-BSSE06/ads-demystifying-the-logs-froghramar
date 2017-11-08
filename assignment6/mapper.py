#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		ip, hp1, hp2, dateTime, gmt, req, path, req_type, status, val = data
		splited_array = dateTime.split("/")
		if len(splited_array) == 3:
			date = splited_array[2]
			re_splited_array = date.split(":")
			if len(re_splited_array) == 4:
				year = re_splited_array[0]
				print "{0}".format(year)


