from google.oauth2 import service_account
from google.cloud import billing_v1
import json
key_path = '/Users/egatchal/CloudExpert/pricingcheck-436202-f19db4cf7f31.json'

credentials = service_account.Credentials.from_service_account_file(key_path)
client = billing_v1.CloudCatalogClient(credentials=credentials)

def list_compute_skus():
    # Google Compute Engine service ID
    compute_service_id = '6F81-5844-456A'
    parent = f'services/{compute_service_id}'
    
    # Retrieve SKUs for the Compute Engine service
    skus = client.list_skus(parent=parent)
   
    with open("GoogleSKUs.json", "w") as file:
        json.dump(skus, file)
    # for sku in skus:
    #     print(sku)
    #     # print(f'SKU ID: {sku.id}')
    #     # print(f'Display Name: {sku.display_name}')
    #     # for pricing_info in sku.pricing_info:
    #     #     print(f' - Pricing Expression: {pricing_info.pricing_expression}')
    #     #     for tier in pricing_info.pricing_expression.tiers:
    #     #         print(f'   - Tier: {tier.start_unit} - {tier.end_unit} at {tier.unit_price.nanos / 1e9} {tier.unit_price.currency_code}')

def list_services():
    services = client.list_services()
    
    with open("GoogleServices.json", "w") as file:
        json.dump(services, file)

# Call the function to list services
# list_services()

list_compute_skus()
