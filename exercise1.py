#!/usr/bin/env python

import re
from pprint import pprint

sArpTable = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.220.88.1            67   0062.ec29.70fe  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.20           29   c89c.1dea.0eb6  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.22            -   a093.5141.b780  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.37          104   0001.00ff.0001  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.38          161   0002.00ff.0001  ARPA   GigabitEthernet0/0/0
"""

# Strip leading/trailing whitespace from text:
sArpTable = sArpTable.strip()

# Create a list, with each line in the ARP Table in a separate element:
lArpTable = sArpTable.splitlines()

# Create an empty list, and populate it with Dictionaries parsed from the input list:
lStructuredArpTable = []
for sArpEntry in lArpTable:
	# (Exclude the header line)
	if re.search(r"^Protocol", sArpEntry):
		continue
	# (Parse the ARP Entry into pieces, store in dictionary)
	_, sIPAddr, _, sMACAddr, _, sInterfaceName = sArpEntry.split()
	dArpEntry = {"mac_addr": sMACAddr, "ip_addr": sIPAddr, "interface": sInterfaceName}
	# (Append the dictionary onto the output list)
	lStructuredArpTable.append(dArpEntry)

print("Structured ARP Table:")
print("-" * 50)
pprint(lStructuredArpTable)
print("-" * 50)
