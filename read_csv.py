#!/usr/bin/env python3

import csv
with open('hosts.csv') as hosts:
	reader = csv.DictReader(hosts)
	for row in reader:
		print(("{} has {} users").format(row["name"], row["users"]))
		