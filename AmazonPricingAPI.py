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

with open("AmazonServices.json", "w") as file:
    json.dump(response, file)