#!/usr/bin/python

import sys

years = ["2009", "2010", "2011"]
counter = dict()

for line in sys.stdin:
	year = line.strip()
	if year in years:
		counter[year] = counter.get(year, 0) + 1

for year in years:
	print "{0}\t{1}".format(year, counter.get(year, 0))

