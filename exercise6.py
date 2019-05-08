#!/usr/bin/env python

import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

# Read in the YAML file from the home directory:
with open("../../.netmiko.yml", "r") as f:
	dRouterData = yaml.load(f, Loader=yaml.FullLoader)

# Reduce the data down to just the stuff relevant to Cisco4:
dRouterData = dRouterData["cisco4"]

# Use NetMiko to connect to the router and fetch the running config:
myLabHandler = ConnectHandler(**dRouterData)
sRouterConfig = myLabHandler.send_command("show run")

# Parse the config and display all configured IP addresses:
oRouterObj = CiscoConfParse(sRouterConfig.splitlines())
# (Look for interface config blocks that are missing "no ip address")
lInterfaceBlocks = oRouterObj.find_objects_wo_child(parentspec=r"^interface", childspec=r"no ip address")
for oInterfaceBlock in lInterfaceBlocks:
	# (Look for exact lines in the config block that contain "ip address" and display them)
	lIPAddresses = oInterfaceBlock.re_search_children("ip address")
	if(len(lIPAddresses) > 0):
		print("Interface Line: " + oInterfaceBlock.text)
		for oIPAddress in lIPAddresses:
			print("IP Address Line: " + oIPAddress.text)
		print()
