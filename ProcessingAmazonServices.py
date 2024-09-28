"""
Python script to extract certain features from AWS EC2 Instance data
"""
import json
f = open("AmazonServices.json", "r+")
services = json.load(f)
f.close()
# print(services[0].keys())

# print(services[0]["serviceCode"])

# print(services[0]["product"]["attributes"].keys())

# print(services[0]["terms"])

# print(services[0]["version"])

# print(services[0]["publicationDate"])

def ExtractVmInfo(vm_dict):
    """
    Extract features from product attributes
    vCPUs, Memory, Storage, OS, CS, InstanceType, RegionCode
    """

    vmInfo = {
        "vCPUs": vm_dict["product"]["attributes"].get("vcpu", None),
        "Memory": vm_dict["product"]["attributes"].get("memory", None),
        "Storage": vm_dict["product"]["attributes"].get("storage", None),
        "NetworkPerformance": vm_dict["product"]["attributes"].get("networkPerformance", None),
        "OperatingSystem": vm_dict["product"]["attributes"].get("operatingSystem", None),
        "PhysicalProcessor": vm_dict["product"]["attributes"].get("physicalProcessor", None),
        "ClockSpeed": vm_dict["product"]["attributes"].get("clockSpeed", None),
        "InstanceType": vm_dict["product"]["attributes"].get("instanceType", None),
        "InstanceFamily": vm_dict["product"]["attributes"].get("instanceFamily", None),
        "DedicatedEbsThroughput": vm_dict["product"]["attributes"].get("dedicatedEbsThroughput", None),
        "Tenancy": vm_dict["product"]["attributes"].get("tenancy", None),
        "ProcessorFeatures": vm_dict["product"]["attributes"].get("processorFeatures", None),
        "EnhancedNetworkingSupported": vm_dict["product"]["attributes"].get("enhancedNetworkingSupported", None),
        "Location": vm_dict["product"]["attributes"].get("location", None),
        "RegionCode": vm_dict["product"]["attributes"].get("regionCode", None),
        "MarketOption": vm_dict["product"]["attributes"].get("marketoption", None),
        "PreInstalledSoftware": vm_dict["product"]["attributes"].get("preInstalledSw", None)
    }
    
    return vmInfo

print(ExtractVmInfo(services[0]))

