#!/usr/bin/env python

from pprint import pprint
import json

# Read in ARP JSON data from input file:
with open("exercise4_input.txt", "r") as f:
        dArpTableData = json.load(f)

# Create an empty dictionary for adding entries:
dArpEntries = {}

# Parse through the ARP Table data, and append neighbor entries to that dictionary:
for dNeighborData in dArpTableData["ipV4Neighbors"]:
	sIPv4Address = dNeighborData["address"]
	sMACAddress = dNeighborData["hwAddress"]
	dArpEntries[sIPv4Address] = sMACAddress

print("ARP Table Entries:")
print("-" * 50)
pprint(dArpEntries)
print("-" * 50)

