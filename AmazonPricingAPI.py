"""
Code for accessing Amazon Pricing API
Im going to end up just doing amazon and helping undergraduate researchers compute big models
Keep instance type, cpus, memory, cost, etc
"""

import boto3, json
from botocore.config import Config

# Configuration for the AWS Pricing API client
my_config = Config(
    region_name='us-east-1',
    retries={'max_attempts': 10}
)

client = boto3.client('pricing', config=my_config)

# Retrieve service details
# response = client.describe_services(ServiceCode='AmazonEC2') 

# Retrieve product details
response = client.get_products(ServiceCode='AmazonEC2') 
priceList = response["PriceList"]
for i in range(len(priceList)):
    priceList[i] = eval(priceList[i])
with open("AmazonServices.json", "w") as f:
    json.dump(priceList, f, indent=2)