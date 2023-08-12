import requests
import valo_api as val
import json
import functions as f
import episodeAb as episodeAb

response = f.setupRequest()

# Process the response here
text = json.dumps(response.json(), sort_keys = True, indent = 4)
data = json.loads(text)

f.obtainPeakRank(data)

# print(f.obtainRank(data))
