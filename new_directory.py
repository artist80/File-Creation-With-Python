#!/usr/bin/env python3

import os

def new_directory(directory, filename):
	# Before creating a new directory, check to see if it already exists
	if not os.path.isdir(directory):
		os.mkdir(directory)

	# Create the new file inside the new directory
	os.chdir(directory)
	with open(filename, "w") as file:
		pass

	# Return the list of files in the new directory
	file_list = os.listdir()
	return file_list

print(new_directory("PythonPrograms", "script.py"))






# The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory.