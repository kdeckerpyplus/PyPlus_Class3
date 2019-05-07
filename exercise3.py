#!/usr/bin/env python

from pprint import pprint
import json

# Read in NAPALM JSON data from input file:
with open("exercise3_input.txt", "r") as f:
	dNapalmData = json.load(f)

pprint(dNapalmData)

# Create empty IP Address lists:
ipv4_list = []
ipv6_list = []

# Parse the NAPALM dictionary and save off IP addresses to the list:
for sInterfaceName, dAddresses in dNapalmData.items():
	# (Check for IPv4 addresses)
	if "ipv4" in dAddresses.keys():
		dIPv4Addresses = dAddresses["ipv4"]
		for sIPv4Address, dIPv4PrefixInfo in dIPv4Addresses.items():
			ipv4_list.append(sIPv4Address + "/" + str(dIPv4PrefixInfo["prefix_length"]))
	# (Check for IPv6 addresses)
	if "ipv6" in dAddresses.keys():
		dIPv6Addresses = dAddresses["ipv6"]
		for sIPv6Address, dIPv6PrefixInfo in dIPv6Addresses.items():
			ipv6_list.append(sIPv6Address + "/" + str(dIPv6PrefixInfo["prefix_length"]))


# DEBUG output to check lists:
print()
print("IPv4 Addresses:")
print("-" * 50)
pprint(ipv4_list)
print("-" * 50)
print()
print("IPv6 Addresses:")
print("-" * 50)
pprint(ipv6_list)
print("-" * 50)
print()
