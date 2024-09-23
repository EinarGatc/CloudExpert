import json
f = open("AmazonServices.json", "r+")

data = json.load(f)
res = eval(data["PriceList"][0])
print(res.keys())
f.close()