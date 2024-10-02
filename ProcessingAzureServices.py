"""
Python script to extract certain features from Azure Virtual Machines data
Will need to extract more information from Azure Virtual Machines
Need data on VM, cpus, memory, etc
Use other API to obtain data about a VM with a specific ID
"""
import json
f = open("AzureServices.json", "r+")
data = json.load(f)
f.close()
services = data["Items"]
print(services)
