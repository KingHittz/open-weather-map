"""used for importing mutiple api"""

import requests

r = requests.get("http://api.citybik.es/v2/networks", timeout=10)
print(r)

d = requests.get("http://api.citybik.es/v2/networks/velobike-moscow", timeout=10)
print(d.json())

"""automatically populate elo bike- moscow with some other id"""
