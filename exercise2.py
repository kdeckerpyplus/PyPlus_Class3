#!/usr/bin/env python

from pprint import pprint
import yaml

# Create dictionaries for four lab devices (but don't use real usernames/passwords):
dArista4 = {"device_name": "arista4", "host": "arista4.lasthop.io", "username": "fakeuser", "password": "fakepass"}
dSRX2 = {"device_name": "srx2", "host": "srx2.lasthop.io", "username": "fakeuser", "password": "fakepass"}
dNXOS1 = {"device_name": "nxos1", "host": "nxos1.lasthop.io", "username": "fakeuser", "password": "fakepass"}
dNXOS2 = {"device_name": "nxos2", "host": "nxos2.lasthop.io", "username": "fakeuser", "password": "fakepass"}

# Create a list of those dictionaries:
lDevices = [dArista4, dSRX2, dNXOS1, dNXOS2]

#pprint(lDevices)

# Dump the structured data to a YAML file:
with open("exercise2.yml", "w+") as f:
	yaml.dump(lDevices, f, default_flow_style=False)
