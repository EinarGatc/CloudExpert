from google.oauth2 import service_account
from google.cloud import billing_v1
from google.auth import default
from google.protobuf.json_format import MessageToDict
import json, requests
import requests

key_path = '/Users/egatchal/CloudExpert/pricingcheck-436202-f19db4cf7f31.json'

credentials = service_account.Credentials.from_service_account_file(key_path)
print(credentials.token)
# client = billing_v1.CloudCatalogClient(credentials=credentials)

# Set the service ID
service_id = 'services/6F81-5844-456A'

# Prepare the request
url = f'https://cloudbilling.googleapis.com/v1/{service_id}/skus'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Accept': 'application/json'
}

# Make the request
response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    skus = response.json()
    print(skus)
else:
    print(f'Error: {response.status_code} - {response.text}')