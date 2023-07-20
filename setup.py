import requests
import valo_api as val
import json
import functions as f

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

api_key = "HDEV-183d6f00-e6ce-40db-adf1-536792261886"
url = "https://staging-api.henrikdev.xyz"

name = f.getNameTag()
urlExt = f.chooseType()

url = url + urlExt
url = url + name[1] + "/" + name[2]

print(url)

headers = {
    "Authorization": api_key,
}

response = requests.get(url, headers=headers)

# Process the response here

text = json.dumps(response.json(), sort_keys = True, indent = 4)
data = json.loads(text)
print(data)