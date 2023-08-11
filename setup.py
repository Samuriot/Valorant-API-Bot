import requests
import valo_api as val
import json
import functions as f

api_key = input("Please enter your api key: ")
url = "https://api.henrikdev.xyz"

headers = {
    "Authorization": api_key,
}

temp = f.getNameTag();
player_uid = f.getNameID(temp);
url_extension = f.chooseType();

url += url_extension + "na/" + player_uid
print(url)
response = requests.get(url, headers=headers)

# Process the response here
text = json.dumps(response.json(), sort_keys = True, indent = 4)
data = json.loads(text)

print(f.obtainRank(data))
