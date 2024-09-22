import requests
import json

# Azure Retail Prices API URL
url = 'https://prices.azure.com/api/retail/prices'

# Define query parameters to filter for Virtual Machines
params = {
    '$filter': "serviceName eq 'Virtual Machines'"
}

# Send GET request to Azure Prices API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Pretty print the JSON response
    with open('AzureServices.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Pricing data saved to AzureServices.json")
else:
    print(f"Error: {response.status_code} - {response.text}")