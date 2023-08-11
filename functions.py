# managing url extension

from enum import Enum
import requests
import json

api_key = "HDEV-183d6f00-e6ce-40db-adf1-536792261886"
url = "https://api.henrikdev.xyz"

headers = {
    "Authorization": api_key,
}

def chooseType():
    choice = input("Select which type of request you would like: ")
    choice = int(choice)
    match choice:
        # general account info
        case 1:
            return "/valorant/v1/account/"
        # competitive match history
        case 2:
            return "/valorant/v1/by-puuid/lifetime/mmr-history/"
        # previous match history
        case 3:
            return "/valorant/v1/by-puuid/mmr/"
        # get current featured shop
        case 4:
            return "/valorant/v1/store-featured/"
        case _:
            return "/"
        
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    
def getNameTag():
    name = input("Please input your Riot ID: ")
    region = input("Please select your region: ")
    tag = name.partition("#")
    return [tag[0], tag[2], region]

def getNameID(obj):
    web = url + "/valorant/v1/account/"
    web += obj[0] + '/' + obj[1]
    print(web)
    request = requests.get(web, headers=headers)
    text = json.dumps(request.json(), sort_keys = True, indent = 4)
    data = json.loads(text)
    jprint(data)
    return data["data"]["puuid"]

def obtainRank(json_parse):
    rank = json_parse["data"]["currenttierpatched"]
    currentRR = json_parse["data"]["elo"] % 100
    return [rank, currentRR]