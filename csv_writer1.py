#!/usr/bin/env python3

import csv
hosts = [["workstation", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
	writer = csv.writer(hosts_csv)
	writer.writerows(hosts)




# Create a file of "hosts.csv" by using "touch hosts.csv" command if you want this code to run smoothly.