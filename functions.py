# managing url extension

from enum import Enum

def chooseType():
    choice = input("Select which type of request you would like: ")
    choice = int(choice)
    match choice:
        # general account info
        case 1:
            return "/valorant/v1/account/"
        # competitive match history
        case 2:
            return "/valorant/v1/lifetime/mmr-history/"
        # previous match history
        case 3:
            return "/valorant/v1/lifetime/matches/"
        # get current featured shop
        case 4:
            return "/valorant/v1/store-featured/"
        case _:
            return "/"

def getNameTag():
    name = input("Please input your Riot ID: ")
    tag = name.partition("#")
    return {1:tag[0], 2:tag[2]}

