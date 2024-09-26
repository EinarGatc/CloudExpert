"""
Python script to extract certain features from AWS EC2 Instance data
"""
import json
f = open("AmazonServices.json", "r+")
services = json.load(f)
f.close()
# print(services[0].keys())

print(services[0]["serviceCode"])

print(services[0]["product"]["attributes"].keys())

# print(services[0]["terms"])

# print(services[0]["version"])

# print(services[0]["publicationDate"])

"""
product
    productFamily
    sku
    attributes
        vcpu
        memory
        dedicatedEbsThoughput
        operatingSystem
        regionCode
        processorArchitecture
        instanceType

"""