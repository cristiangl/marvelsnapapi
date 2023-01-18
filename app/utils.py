import json


def readDataBase ():

    f = open('./db/database.json')

    data = json.load(f)

    return data

def findCardInDB(name, db):
    for card in db:
        if card['name'].lower() == name:
            return card
    
    return None