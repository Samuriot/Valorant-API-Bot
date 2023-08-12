# managing url extension

from enum import Enum
import requests
import json
import episodeAb as ep

api_key = "HDEV-183d6f00-e6ce-40db-adf1-536792261886"
url = "https://api.henrikdev.xyz"

headers = {
    "Authorization": api_key,
}

def chooseUrlType():
    print("\nFor General Account Info: 1")
    print("Competitive Match History: 2")
    print("Previous Match History: 3")
    print("Current Featured Shop: 4")
    choice = input("Select which type of request you would like: ")
    choice = int(choice)
    match choice:
        # general account info
        case 1:
            return "/valorant/v1/account/"
        # competitive match history
        case 2:
            return "/valorant/v2/by-puuid/mmr/"
        # previous match history
        case 3:
            return "/valorant/v3/by-puuid/matches/"
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
    request = requests.get(web, headers=headers)
    text = json.dumps(request.json(), sort_keys = True, indent = 4)
    data = json.loads(text)
    return data["data"]["puuid"]

def obtainRank(json_parse):
    rank = json_parse["data"]["currenttierpatched"]
    currentRR = json_parse["data"]["elo"] % 100
    return [rank, currentRR]

def obtainPeakRank(json_parse):
    highestRank = json_parse["data"]["highest_rank"]["patched_tier"]
    highestRankSeason = json_parse["data"]["highest_rank"]["season"]
    print(highestRank + " in " + ep.getEpisodeAct(highestRankSeason))
    return [highestRank, highestRankSeason]

def setupRequest():
    api_key = input("Please enter your api key: ")
    url = "https://api.henrikdev.xyz"

    headers = {
        "Authorization": api_key,
    }

    player_tag = getNameTag();
    player_uid = getNameID(player_tag);
    url_extension = chooseUrlType();

    url += url_extension + "na/" + player_uid
    print(url)
    return requests.get(url, headers=headers)
