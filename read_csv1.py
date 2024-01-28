#!/usr/bin/env python3

import csv
f = open("csv_file.txt")
csv_f = csv_reader(f)
for row in csv_f:
	name, phone, role = row
	print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

f.close()




# You should have file "csv_file.txt" to run this code smoothly.

# Add this content:
 # Sabrina Green,802-867-5309,System Administrator
 # Eli Jones,695-3275393-2832,IT Specialist
 # Melody Daniels,8392-283742891,Programmer
 # Charlie Rivera,3829-1838-187328,Web Developer