import requests
import json
#import logging

# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)

# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

ip = requests.get("http://api.ipify.org")

print(ip.text)



zoneId = "5f5b0bf2ebe816578be8c5553c98be6d"
apiToken = "fupBXzTMFsmgAxcna8ZTcmHnsX5dRznK2QtSSPl_"
apiKey = "58ec6020b9886fd8e30275b55ddc8b3c79bea"
apiEmail = "christoph.califice@hotmail.com"

url_getEntries = f"https://api.cloudflare.com/client/v4/zones/{zoneId}/dns_records"
url_updateEntry = f"https://api.cloudflare.com/client/v4/zones/{zoneId}/dns_records/"
reqHeaders = {
    #"Authorization": "Bearer " + apiToken,
    "X-Auth-Email": apiEmail,
    "X-Auth-Key": apiKey
    }


req = requests.get(url_getEntries, headers=reqHeaders)



entriesJson = json.loads(req.text)


for entry in entriesJson["result"]:
    if(entry["type"] == "A"):
        id = entry["id"]
        name = entry["name"]

        data = {
            "content": f"{ip.text}",
            "name": f"{name}",
            "ttl": "1"      
        }

        print(data)

        resp = requests.patch(url_updateEntry + id, json=data,  headers=reqHeaders)
        print(resp.text)

  