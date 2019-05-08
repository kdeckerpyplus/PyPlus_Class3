#!/usr/bin/env python

import yaml
from netmiko import ConnectHandler

# Read in the YAML file from the home directory:
with open("../../.netmiko.yml", "r") as f:
	dRouterData = yaml.load(f, Loader=yaml.FullLoader)

# Reduce the data down to just the stuff relevant to Cisco3:
dRouterData = dRouterData["cisco3"]

# Use NetMiko to connect to the router and display the prompt:
myLabHandler = ConnectHandler(**dRouterData)
sRouterPrompt = myLabHandler.find_prompt()
print(sRouterPrompt)

