#!/usr/bin/env python3

import os
import datetime

def file_date(filename):
	# Create tje file in the current directory
	with open(filename, "w") as file:
		pass

	# Get the current timestamp
	timestamp = os.path.getmtime(filename)

	# Convert the timestamp into a readable format, then into a string
	date = datetime.datetime.fromtimestamp(timestamp).date()
	date_string = str(date)

	# Return just the date portion
	return date_string

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd



# The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. 