#!/usr/bin/python

import sys

cnt_map = dict()

for line in sys.stdin:
	path = line.strip()
	cnt_map[path] = cnt_map.get(path, 0) + 1

print len(cnt_map)

