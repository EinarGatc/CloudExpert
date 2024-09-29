"""
Python script to extract certain features from Google Cloud Compute Instance data
"""
import json
f = open("GoogleServices.json", "r+")

data = json.load(f)
services = data["skus"]
print(services)

f.close()