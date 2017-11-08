#!/usr/bin/python

import sys

cnt_map = dict()

for line in sys.stdin:
	path = line.strip()
	cnt_map[path] = cnt_map.get(path, 0) + 1

max_path = max(cnt_map, key=cnt_map.get)
max_cnt = cnt_map.get(max_path, 0)

print "{0}\t{1}".format(max_path, max_cnt)

